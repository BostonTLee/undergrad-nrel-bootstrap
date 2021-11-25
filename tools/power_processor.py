"""Provides a class encapsulating power processing calculations."""
import numpy as np

from astronomical_adjustment import AstronomicalAdjustment as aa
from pv_module import PVModule as pvm


class PowerProcessor:
    """Provides an interface for power processing calculation."""

    @classmethod
    def ideal_power(
        cls,
        ideality,
        temperature,
        sc_current_module,
        i_eff,
        n_parallel,
        n_series,
        oc_voltage,
    ):
        """Returns the ideal maximum power output from the grid.

        Power is maximized over 20 values of voltage,
        as found in the source included with the paper

        Args:
            n_parallel (int): The number of PV cells connected in parallel
            n_series (int): The number of PV cells connected in series
            i_out (float): The output current from a PV module

        Returns:
            float: Returns the ideal maximum power output from the grid

        """
        # This method of maximization was found in the source
        # code for the paper
        N_SAMPLES = 20
        voltage_vec = np.linspace(0, oc_voltage, N_SAMPLES)

        # Nested function so we can easily create a vectorized function
        def get_current_output(voltage):
            return pvm.current_output(
                voltage,
                ideality,
                temperature,
                sc_current_module,
                oc_voltage,
                i_eff,
                n_parallel,
                n_series,
            )

        vectorized_get_current_output = np.vectorize(get_current_output)
        current_vec = vectorized_get_current_output(voltage_vec)
        vec_to_be_maximized = (
            n_parallel * n_series * np.multiply(current_vec, voltage_vec)
        )
        max_index = np.argmax(vec_to_be_maximized)
        # Return the *current* corresponding to the max power
        return current_vec.item(max_index)

    @classmethod
    def estimated_power(
        cls,
        ideality,
        temperature,
        sc_current_module,
        i_eff,
        n_parallel,
        n_series,
        oc_voltage,
        efficiency,
    ):

        """Returns the estimated processed power output the grid.

        The value of `i_out` is determined using the PVModule class.
        Source paper assumes efficiency=.5

        Args:
            n_parallel (int): The number of PV cells connected in parallel
            n_series (int): The number of PV cells connected in series
            i_out (float): The output current from a PV module
            voltage (float): The solar cell voltage
            efficiency (float): The conversion efficiency of the power processor used

        Returns:
            float: Returns the estimated processed power output from the grid

        """
        max_power = cls.ideal_power(
            ideality,
            temperature,
            sc_current_module,
            i_eff,
            n_parallel,
            n_series,
            oc_voltage,
        )
        return efficiency * max_power
