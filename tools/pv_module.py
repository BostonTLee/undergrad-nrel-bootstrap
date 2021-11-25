"""Provides a class encapsulating current output calculations from the photovoltaic module."""
import math


class PVModule:
    """Provides an interface for current output calculation.

    Attributes:
        q (float): The elementary charge in coulombs
        k (float): Boltzmann's constant

    """

    q = 1.6e-19
    k = 1.38e-23

    @classmethod
    def radiation_rate(cls, i_eff):
        """Returns the radiation rate of a photovoltaic module.

        The value of `i_eff` is determined using the AstronomicalAdjustment class.

        Args:
            i_eff (float): Effective solar irradiance

        Returns:
            float: Returns the radiation rate constant

        """
        return 0.0001 * i_eff

    @classmethod
    def light_generated_current(cls, sc_current, i_eff):
        """Return the current generated from light in a photovoltaic module.

        The value of `i_eff` is determined using the AstronomicalAdjustment class. A reasonable value for sc_current was given in the source paper.

        Args:
            sc_current (float): Short circuit current- the maximum current of the system
            i_eff (float): Effective solar irradiance

        Returns:
            float: Returns the current generated from light in a photovoltaic module in coulombs

        """
        F = cls.radiation_rate(i_eff)
        return sc_current * F

    @classmethod
    def convert_temperature(cls, temperature):
        """Converts temperature from degrees Celsius to degress Kelvin.

        Degrees Kelvin specified in source paper.

        Args:
            temperature (int): Temperature in degrees Celsius

        Returns:
            float: Returns the temperature in degrees Kelvin

        """
        return temperature + 273.15

    @classmethod
    def current_output(
        cls,
        voltage,
        ideality,
        temperature,
        sc_current_module,
        oc_voltage,
        i_eff,
        n_parallel,
        n_series,
    ):
        """Return the current output of a photovoltaic module.

        The value of `i_eff` is determined using the AstronomicalAdjustment class.

        Leakage is calculated using the logic from the code for the project in
        the paper.  The calculations for this quantity is not described in the
        paper.

        Source paper assumes sc_current=5
        Source paper (code) assumes ideality=1.5

        Where does voltage come from?
        It appears voltage is adjusted as part of the MPPT algorithm;
        we are maximizing over voltage, where voltage <= v_oc.


        Args:
            voltage (float): The cell voltage, less than the OC voltage
            ideality (float):
            temperature (int): Temperature in degrees Celsius
            sc_current_module (float): Short circuit current
                of a solar module- the maximum current of the system
            i_eff (float): Effective solar irradiance
            n_parallel (int): The number of panels in parallel
            n_series (int): The number of groups of panels in series

        Returns:
            float: Returns the current output of a photovoltaic module in coulombs

        """
        q = cls.q
        k = cls.k
        temperature_kelvin = cls.convert_temperature(temperature)

        sc_current_single_cell = sc_current_module / n_parallel
        oc_voltage_single_cell_ref = oc_voltage / n_series
        leakage = (sc_current_single_cell) / (
            math.exp(
                q
                * (oc_voltage_single_cell_ref)
                / (ideality * k * temperature_kelvin)
            )
        )
        # oc_voltage_module = (ideality * k * (temperature) / q) * (
        #     math.log(sc_current_module / leakage + 1)
        # )
        # oc_voltage_single_cell = oc_voltage_module / n_series

        light_current = cls.light_generated_current(
            sc_current_single_cell, i_eff
        )
        return light_current - leakage * (
            math.exp(q * voltage / ideality * k * temperature) - 1
        )
