import functools
from multiprocessing.pool import ThreadPool
from typing import Callable, Dict, Iterable, List, Tuple, Union

from .settings import FINTOOLS_DEFAULT_THREADS


class ConcurrentFunction:

    def __init__(self, function: Callable):
        self.function = function
        functools.update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

    def run(self, *args, **kwargs):
        return self.function(*args, **kwargs)

    def run_safely(self, *args, **kwargs):
        try:
            return {
                "status": "SUCCESS",
                "result": self.run(*args, **kwargs),
                "message": "",
                "args": args,
                "kwargs": kwargs
            }
        except Exception as e:
            return {
                "status": "FAILURE",
                "result": None,
                "message": str(e),
                "args": args,
                "kwargs": kwargs
            }

    def run_over_args(self, iterable: List[Iterable], safely: bool = False) -> List:
        wrapper = self.run if not safely else self.run_safely
        return [
            wrapper(*args)
            for args in iterable
        ]

    def run_over_kwargs(self, iterable: List[Dict], safely: bool = False) -> List:
        wrapper = self.run if not safely else self.run_safely
        return [
            wrapper(**kwargs)
            for kwargs in iterable
        ]

    def run_over(self, iterable: List[Union[Dict, Tuple]], safely: bool = False) -> List:
        first, *_ = iterable
        if isinstance(first, dict):
            return self.run_over_kwargs(iterable=iterable, safely=safely)
        return self.run_over_args(iterable=iterable, safely=safely)

    def run_concurrently_args(
            self,
            iterable: List[Iterable],
            threads: int = FINTOOLS_DEFAULT_THREADS,
            safely: bool = False
    ) -> List:
        with ThreadPool(threads) as pool:
            results = pool.map(
                func=lambda args: self.run(*args) if not safely else self.run_safely(*args),
                iterable=iterable)
        return results

    def run_concurrently_kwargs(
            self,
            iterable: List[Dict],
            threads: int = FINTOOLS_DEFAULT_THREADS,
            safely: bool = False
    ) -> List:
        with ThreadPool(threads) as pool:
            results = pool.map(
                func=lambda kwargs: self.run(**kwargs) if not safely else self.run_safely(*kwargs),
                iterable=iterable
            )
        return results

    def run_concurrently(self, iterable, threads: int = FINTOOLS_DEFAULT_THREADS, safely: bool = False):
        first, *_ = iterable
        if isinstance(first, dict):
            return self.run_concurrently_kwargs(iterable=iterable, threads=threads, safely=safely)
        return self.run_concurrently_args(iterable=iterable, threads=threads, safely=safely)
