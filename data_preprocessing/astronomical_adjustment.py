"""Provides a class encapsulating effective solar irradiance calculations."""
import math

import pandas as pd
import numpy as np


class AstronomicalAdjustment:
    """Provides an interface for effective solar irradiance calculation.

    Attributes:
        BETA (float): The inclination of the solar panel toward the sun on
                the horizon
        ALPHA (float): The azimuthal displacement, calculated from if the
                solar panel faces East or West (see paper for details)

    """

    # Values obtained from paper, for Los Angeles
    BETA = math.radians(45)
    ALPHA = math.radians(30)

    @classmethod
    def d_helper(cls, day_number):
        """Return the value of an internal helper function.

        Internal helper function never given a name in the paper.

        Args:
            day_number (int): Day number of the year, beginning January 1

        Returns:
            float: Value of the helper function, in radians

        """
        d_deg = 360 * (day_number - 81) / 365
        d_rad = math.radians(d_deg)
        return d_rad

    @classmethod
    def declination_angle(cls, day_number):
        """Return the declination angle for a given day.

        The declination angle is the anglular distance to the north
        or south of the equator.

        Args:
            day_number (int): Day number of the year, beginning January 1

        Returns:
            float: Returns the declination angle in radians

        """
        EARTH_ANGLE = math.radians(23.45)
        D = cls.d_helper(day_number)
        return math.asin(math.sin(EARTH_ANGLE) * math.sin(D))

    @classmethod
    def hour_angle(cls, time, day_number, longitude, utc_off):
        """Return the hour angle for a given day and time.

        The hour angle is the angle of the sun's rays given the
        rotation of the Earth.

        Args:
            day_number (int): Day number of the year, beginning January 1

        Returns:
            float: Returns the hour angle in radians

        """
        hour_angle_degrees = (
            15 * cls.apparent_solar_time(time, day_number, longitude, utc_off)
            - 12
        )
        return math.radians(hour_angle_degrees)

    @classmethod
    def apparent_solar_time(cls, time, day_number, longitude, utc_off):
        """Return the apparent solar time (AST) for a given time and location.

        The time msut be specified as a time and day number,
        while the location is given by a longitude and a UTC offset
        from GMT.

        Args:
            time (int): Time of the day, in hours
            day_number (int): Day number of the year, beginning January 1
            longitude (float): The longitude of the location
            utc_off (float): The time offset from UTC (in hours)

        Returns:
            float: Returns the apparent solar time in hours

        """
        gma = utc_off * 15
        time_displacement = (longitude - gma) / 15
        # FIXME adjust for daylight savings?
        return time + time_displacement + cls.equation_of_time(day_number)

    @classmethod
    def equation_of_time(cls, day_number):
        """Return the equation of time for a given day.

        No details are given in the paper as to the significance of the
        equation of time, except that it is used to calcuate AST.

        Args:
            day_number (int): Day number of the year, beginning January 1

        Returns:
            float: Returns the value of the equation of time of a given day number

        """
        D = cls.d_helper(day_number)
        return (
            9.87 * math.cos(2 * D) - 7.53 * math.cos(D) - 1.5 * math.sin(D)
        ) / 60

    @classmethod
    def angle_sun_surface(cls, time, day_number, latitude, longitude, utc_off):
        """Return the cosine of the angle between the sun and the panel surface.

        This is the main helper function used to calcualte effective solar
        irradiance.

        Args:
            time (int): Time of the day, in hours
            day_number (int): Day number of the year, beginning January 1
            latitude (float): The latitude of the location
            longitude (float): The longitude of the location
            utc_off (float): The time offset from UTC (in hours)

        Returns:
            float: Returns the cosine of the angle between the sun and the panel surface

        """
        ALPHA = cls.ALPHA
        BETA = cls.BETA
        declination_angle = cls.declination_angle(day_number)
        hour_angle = cls.hour_angle(time, day_number, longitude, utc_off)
        latitude = abs(math.radians(latitude))
        ret_val = (
            (math.sin(declination_angle) * math.sin(latitude) * math.cos(BETA))
            - (
                math.sin(declination_angle)
                * math.cos(latitude)
                * math.sin(BETA)
                * math.cos(ALPHA)
            )
            + (
                math.cos(declination_angle)
                * math.cos(latitude)
                * math.cos(BETA)
                * math.cos(hour_angle)
            )
            + (
                math.cos(declination_angle)
                * math.sin(latitude)
                * math.sin(BETA)
                * math.cos(ALPHA)
                * math.cos(hour_angle)
            )
            + (
                math.cos(declination_angle)
                * math.sin(BETA)
                * math.sin(ALPHA)
                * math.sin(hour_angle)
            )
        )
        return ret_val

    @classmethod
    def construct_time(cls, hour, minute):
        """Return the 24-hour time.

        This helper funtion uses hour and minute to derive the 24-hour time.

        Args:
            hour (int): Hour of the day
            minute (int): Minute of the hour

        Returns:
            float: Returns the 24-hour time in hours

        """
        return hour + minute / 60

    @classmethod
    def construct_day(cls, month, day):
        """Return the day of the year.

        This helper funtion uses month and day to derive the day of the year.

        Args:
            month (int): Month of the year
            day (int): Day of the month

        Returns:
            int: Returns the day of the year out of 365 (or 366)

        """

        cumulative_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(cumulative_days[0 : int(month)]) + day

    @classmethod
    def effective_solar_radiance(
        cls, i_sun, month, day, hour, minute, latitude, longitude, utc_off
    ):
        """Return the effective solar radiance as a function of time.

        The value of `i_sun` is determined from the NREL database.

        Args:
            i_sun (float): Instantaneous solar radiance
            month (int): Month of the year
            day (int): Day of the month
            hour (int): Hour of the day
            minute (int): Minute of the hour
            latitude (float): The latitude of the location
            longitude (float): The longitude of the location
            utc_off (int): The time offset from UTC (in hours)

        Returns:
            float: Returns the effective solar irradiance in W/m^2

        """

        time = cls.construct_time(hour, minute)
        day_number = cls.construct_day(month, day)

        return i_sun * max(
            0,
            cls.angle_sun_surface(
                time, day_number, latitude, longitude, utc_off
            ),
        )
