from typing import Optional

from fintools import Amortization


class Main:

    @staticmethod
    def annuity(amount: float, rate: float, n: int):
        raise NotImplementedError

    @staticmethod
    def table(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        raise NotImplementedError

    @staticmethod
    def plot(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        raise NotImplementedError
