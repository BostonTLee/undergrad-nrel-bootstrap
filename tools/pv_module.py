"""Provides a class encapsulating current output calculations from the photovoltaic module."""
import math

class PVModule:
    """Provides an interface for current output calculation.

    Attributes:
        q (float): The elementary charge in coulombs
        k (float): Boltzmann's constant

    """

    q = 1.6E-19
    k = 1.38E-23

    def radiation_rate(cls, i_eff):
        """Returns the radiation rate of a photovoltaic module.

        The value of `i_eff` is determined using the AstronomicalAdjustment class.

        Args:
            i_eff (float): Effective solar irradiance

        Returns:
            float: Returns the radiation rate constant
            
        """
        return .0001 * i_eff
    
    def light_generated_current(cls, sc_current, i_eff):
        """Return the current generated from light in a photovoltaic module.

        The value of `i_eff` is determined using the AstronomicalAdjustment class. A reasonable value for sc_current was given in the source paper. 

        Args:
            sc_current (float): Short circuit current- the maximum current of the system
            i_eff (float): Effective solar irradiance

        Returns:
            float: Returns the current generated from light in a photovoltaic module in coulombs

        """
        F = cls.radiation_rate(cls, i_eff)
        return sc_current * F

    def convert_temperature(cls, temperature):
        """Converts temperature from degrees Celsius to degress Kelvin^3.

        Degree Kelvin^3 specified in source paper.

        Args:
            temperature (int): Temperature in degrees Celsius

        Returns:
            float: Returns the temperature in degrees Kelvin^3

        """
        return (temperature + 273.15) ** 3

    def current_output(cls, voltage, ideality, temperature, sc_current, leakage, i_eff):
        """Return the current output of a photovoltaic module.

        The value of `i_eff` is determined using the AstronomicalAdjustment class.

        Args:
            voltage (float): 
            ideality (float): 
            temperature (int): Temperature in degrees Celsius
            leakage (float):
            sc_current (float): Short circuit current- the maximum current of the system
            i_eff (float): Effective solar irradiance 

        Returns:
            float: Returns the current output of a photovoltaic module in coulombs

        """
        q = cls.q
        k = cls.k
        light_current = cls.light_generated_current(cls, sc_current, i_eff)
        temp = cls.convert_temperate(cls, temperature)
        return light_current - leakage * (math.exp(q * voltage / ideality * k * temperature) - 1)


# where do voltage, leakage, and ideality come from?
# source paper assumes sc_current=5


