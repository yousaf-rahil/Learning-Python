from functools import lru_cache
import time
@lru_cache(maxsize=None)
def mul(x):
    time.sleep(5)
    return x*2

print("Round One")
print(mul(10))
print(mul(2))
print(mul(3))

print("Round Two")
print(mul(10))
print(mul(2))
print(mul(3))