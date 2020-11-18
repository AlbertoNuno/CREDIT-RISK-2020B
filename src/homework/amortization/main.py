from typing import Optional
from fintools import Amortization
import pandas as pd
import amortization as am
a= pd.DataFrame()


class Main:

    @staticmethod
    def annuity(amount: float, rate: float, n: int):
        ann = am.Amortization(amount, rate, n)
        return ann.annuity

    @staticmethod
    def table(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        ann = am.Amortization(amount, rate, n)
        return ann.get_table()

    @staticmethod
    def plot(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        to_plot = am.Amortization(amount, rate, n)
        return to_plot.plot()


n: int, save_file: Optional[str] = None):
        raise NotImplementedError
