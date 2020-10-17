from .models import Borrower
import json
from fintools.settings import get_logger

logger = get_logger(name="__main__")
DEFAULT_FILENAME = "C:/Users/anuno/OneDrive/Documents/ITESO/Modelos de crédito/CREDIT-RISK-2020B/src/homework/borrowers/candidates.json"


class Main:

    @staticmethod
    def show(file: str = DEFAULT_FILENAME) -> str:
        # logger.info("Calling the show method.")
        with open(file, "r") as f:
            data = json.load(f)
        return json.dumps(data)

    @staticmethod
    def insert(email: str, age: int, income: float, file: str = DEFAULT_FILENAME):
        borrower = Borrower(email=email, age=age, income=income)
        borrower.save(file=file)

    @staticmethod
    def update(email: str, age: int, income: float, file: str = DEFAULT_FILENAME):
        borrower = Borrower(email=email, age=age, income=income)
        borrower.update(file=file)
