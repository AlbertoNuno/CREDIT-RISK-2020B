from typing import List

import numpy as np


def irr(amounts: List[float]) -> float:
    """
    Internal Rate of return.

    Get the IRR out of an ordered list of cashflow amounts.
    Example:
    cfs = [
        -10000,    # Loan disbursment
        1000,      # Interest payment
        1000,      # Interest payment
        1000,      # Interest payment
        1000,      # Interest payment
        11000,     # Interest + Principal
    ]
    irr_value = irr(amounts=cfs)

    :param amounts: An ordered list of cashflow amounts.
    The position of the amounts should represent the "t" of the cashflows.
    :return: The internal rate of return.
    """
    # Get polynomial roots
    res = np.roots(amounts[::-1])
    # Filter out imaginary component.
    mask = (res.imag == 0) & (res.real > 0)
    if not mask.any:
        return np.nan
    res = res[mask].real
    # Return the solution closest to zero.
    rate = 1 / res - 1
    return rate[np.argmin(np.abs(rate))]
