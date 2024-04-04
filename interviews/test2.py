
from time import time, sleep
from typing import Callable

def time_func(func: Callable) -> Callable:
    def wrapper(*argc, **kwargs):
        start:float = time()
        func(*argc, **kwargs)
        end:float = time() - start
        print('time is',end)
    return wrapper



@time_func
def sleep_time(sec) -> None:
    sleep(sec)

for i in range(10):
    sleep_time(0.1)
    