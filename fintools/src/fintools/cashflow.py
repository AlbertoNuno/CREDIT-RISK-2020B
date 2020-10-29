from typing import Dict, Optional


class CashFlow:

    def __init__(self, amount: float, n: int):
        self.amount = amount
        self.n = n

    def pv(self, r: float) -> 'CashFlow':
        self.amount = self.amount / ((1 + r) ** self.n)
        self.n = 0
        return self

    def shift(self, n: int, r: float) -> 'CashFlow':
        if n > self.n:
            n_ = n - self.n
            self = self.fv(r, n_)
            self.n = n

        elif n < self.n:
            self.n = n
            self = self.pv(r)
        return self

    def merge(self, other: 'CashFlow', r: float, reverse: bool = False) -> 'CashFlow':

        if reverse == False:
            other = other.pv(r)
            t_amt = other.amount + self.amount
            n = self.n
            result = CashFlow(t_amt, n)
        elif reverse == True:
            self = self.fv(r, other.n)
            t_amt = other.amount + self.amount
            n = other.n
            result = CashFlow(t_amt, n)

        return result


    def to_dict(self, decimal_places: Optional[int] = 2) -> Dict:
        return {
            "amount": self.amount if decimal_places is None else round(self.amount, decimal_places),
            "n": self.n
        }

    def fv(self, r: float, n: float) -> 'CashFlow':
        self.amount = self.amount * ((1 + r) ** n)
        self.n = n
        return self



