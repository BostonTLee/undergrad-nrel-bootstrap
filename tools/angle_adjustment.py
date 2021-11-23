import math

import numpy as np


class AstronomicalAngleAdjustment:

    # Values obtained from paper, for Los Angeles
    BETA = math.radians(45)
    ALPHA = math.radians(30)

    def d_helper(cls, day_number):
        d_deg = 360 * (day_number - 81) / 365
        d_rad = math.radians(d_deg)
        return d_rad

    def declination_angle(cls, day_number):
        EARTH_ANGLE = math.radians(23.45)
        C = math.sin(EARTH_ANGLE)
        D = cls.d_helper(day_number)
        return math.arcsin(C * math.sin(D))

    def hour_angle(cls, time, day_number):
        hour_angle_degrees = (
            15 * cls.apparent_solar_time(time, day_number) - 12
        )
        return math.radians(hour_angle_degrees)

    def apparent_solar_time(cls, time, day_number, longitude, utc_off):
        # FIXME
        gma = utc_off * 15
        time_displacement = (longitude - gma) / 15
        # FIXME what is t'?
        return time + time_displacement + cls.equation_of_time(day_number)

    def equation_of_time(cls, day_number):
        D = cls.d_helper(day_number)
        return (
            9.87 * math.sin(2 * D) - 7.53 * math.cos(D) - 1.5 * math.sin(D)
        ) / 60

    def angle_sun_surface(cls, time, day_number, latitude, longitude, utc_off):
        ALPHA = cls.ALPHA
        BETA = cls.BETA
        declination_angle = cls.declination_angle(day_number)
        hour_angle = cls.hour_angle(time, day_number)
        latitude = np.radians(latitude)
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

    def effective_solar_radiance(
        cls, i_sun, time, day_number, latitude, longitude, utc_off
    ):
        return i_sun * math.max(
            0,
            cls.angle_sun_surface(
                cls, time, day_number, latitude, longitude, utc_off
            ),
        )
