"""Provides a class encapsulating power processing calculations."""
import numpy as np


class PowerProcessor:
    """Provides an interface for power processing calculation."""

    def ideal_power(cls, n_parallel, n_series, i_out, voltage):
        """Returns the ideal maximum power output from a photovoltaic module.

        # FIXME
        Power is maximized over ... values of voltage.

        Args:
        # FIXME
            n_parallel (int): The number of PV cells connected in parallel
            n_series (int): The number of PV cells connected in series
            i_out (float): The output current from a PV module
            voltage (float):

        Returns:
            float: Returns the ideal maximum power output from a photovoltaic module

        """
        return n_parallel * n_series * np.max(i_out * voltage)

    def estimated_power(cls, n_parallel, n_series, i_out, voltage, efficiency):
        """Returns the estimated processed power output from a photovoltaic module.

        The value of `i_out` is determined using the PVModule class.

        Args:
        # FIXME
            n_parallel (int): The number of PV cells connected in parallel
            n_series (int): The number of PV cells connected in series
            i_out (float): The output current from a PV module
            voltage (float):
            efficiency (float): The conversion efficiency of the power processor used

        Returns:
            float: Returns the estimated processed power output from a photovoltaic module

        """
        max_power = cls.ideal_power(cls, n_parallel, n_series, i_out, voltage)
        return efficiency * max_power


# what range of voltages am I maximizing over?
# source paper assumes efficiency=.5
