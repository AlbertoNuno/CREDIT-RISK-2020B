from .models import Borrower
from fintools.settings import get_logger
import json
from .utils import get_current_utc
logger = get_logger(name="__main__")
DEFAULT_FILENAME = "./borrowers/candidates.json"


class Main:

    @staticmethod
    def show(file: str = DEFAULT_FILENAME) -> str:
        logger.info("Calling the show method.")
        with open (file,"r") as f:
            data = json.load(file)
        return json.dumps(data)

    @staticmethod
    def insert(email: str, age: int, income: float, file: str = DEFAULT_FILENAME):

        borrower = Borrower(email=email, age=age, income=income)
        new_file = borrower.save(file=file)
        return new_file



    @staticmethod
    def update(email: str, age: int, income: float, file: str = DEFAULT_FILENAME):
        borrower = Borrower(email=email, age=age, income=income)
        borrower.update(file=file)
