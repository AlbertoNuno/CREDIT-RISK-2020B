from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Amortization:

    def __init__(self, amount: float, rate: float, n: int):
        self.amount = amount
        self.rate = rate
        self.n = n

    @property
    def annuity(self) -> float:
        raise NotImplementedError

    def get_table(self, save_file: Optional[str] = None) -> pd.DataFrame:
        raise NotImplementedError

    def plot(self, show: bool = False, save_file: Optional[str] = None) -> None:
        raise NotImplementedError
