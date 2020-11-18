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
        return (self.amount * self.rate) / (1 - (1 + self.rate) ** (-self.n))

    def get_table(self, save_file: Optional[str] = None) -> pd.DataFrame:
        def pv(n):
            return self.annuity * ((1 - (1 + self.rate) ** (-n)) / self.rate)

        def payment(table, i):
            if i > 0:
                payment = self.annuity - (table["B"][i - 1] * self.rate)
                interest = table["B"][i - 1] * self.rate
            else:
                interest = None
                payment = None
            return payment, interest

        period_zero = lambda t, value: value if t > 0 else None

        table = pd.DataFrame()
        table["t"] = list(i for i in range(0, self.n + 1))
        table["B"] = list(pv(self.n - i) for i in range(0, self.n + 1))
        table["A"] = list(period_zero(i, self.annuity) for i in range(0, self.n + 1))
        table["P"] = list(payment(table, i)[0] for i in range(0, self.n + 1))
        table["I"] = list(payment(table, i)[1] for i in range(0, self.n + 1))

        if save_file != None:
            table.to_csv(save_file)

        return table

    def plot(self, show: bool = False, save_file: Optional[str] = None) -> None:
        am_table = self.get_table()
        payment = am_table["P"].fillna(0)
        interest = am_table["I"].fillna(0)
        index = np.arange(0, self.n + 1)
        plt.bar(index, payment, label='Payment')
        plt.bar(index, interest, label='Interest', bottom=payment)
        plt.legend(loc='best')
        plt.title("Amortization Payment")
        plt.xlabel("t")
        plt.ylabel("$$$")
        plt.grid()

        if show == True:
            plt.show()

        if save_file != None:
            plt.savefig(save_file)


