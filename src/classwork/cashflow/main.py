import json

from fintools import CashFlow


class Main:

    @staticmethod
    def present_value(amount: float, rate: float, n: int):
        flow = CashFlow(amount,n)
        flow = flow.pv(rate)
        return flow.to_dict()

    @staticmethod
    def future_value(amount: float, rate: float, n: int):
        flow = CashFlow(amount,n)
        flow = flow.fv(rate,n)
        return flow.to_dict()


