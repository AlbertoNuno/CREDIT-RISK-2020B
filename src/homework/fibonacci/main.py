from typing import List
from fintools.src.fintools.settings import get_logger
from fintools.src.fintools.settings import timeit
from fintools.src.fintools.utils import method_catching
logger = get_logger(name=__name__)


class Main:

    def __init__(self):
        logger.info("Main object initialized.")
    @method_catching
    def element(self, position: int) -> int:
        if position ==0:
            return 0
        elif position ==1:
            return 1
        else :
            return self.element(position-1) + self.element(position-2)

    @timeit
    def sequence(self, length: int) -> List[int]:
        sequence  = list(self.element(i) for i in range(0,length+1))
        return sequence
