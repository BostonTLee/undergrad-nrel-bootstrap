"""Provides a class encapsulating power processing calculations."""
import numpy as np


class PowerProcessor:
    """Provides an interface for power processing calculation."""

    def ideal_power(cls, n_parallel, n_series, i_out, sc_voltage):
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
        voltage_vec = np.linspace(0, sc_voltage, N_SAMPLES)
        # FIXME i_out nees to be a vector
        return n_parallel * n_series * np.amax(i_out * voltage_vec)

    def estimated_power(cls, n_parallel, n_series, i_out, voltage, efficiency):
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
        max_power = cls.ideal_power(cls, n_parallel, n_series, i_out, voltage)
        return efficiency * max_power
