from concurrent.futures import ThreadPoolExecutor
import time
from concurrent.futures import ProcessPoolExecutor
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

NUMBERS = [
   2,
   1099726899285419,
   1570341764013157,
   1637027521802551,
   1880450821379411,
   1893530391196711,
   2447109360961063,
   3,
   2772290760589219,
   3033700317376073,
   4350190374376723,
   4350190491008389,
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,
]

def filter_primes_threadpool(numbers):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    primes = [num for num, prime in zip(numbers, results) if prime]
    return primes

def filter_primes_processpool(numbers):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    primes = [num for num, prime in zip(numbers, results) if prime]
    return primes

start_time = time.time()
primes_threadpool = filter_primes_threadpool(NUMBERS)
threadpool_duration = time.time() - start_time

start_time = time.time()
primes_processpool = filter_primes_processpool(NUMBERS)
processpool_duration = time.time() - start_time

print("ThreadPoolExecutor primes:", primes_threadpool)
print("ThreadPoolExecutor duration:", threadpool_duration)
print("ProcessPoolExecutor primes:", primes_processpool)
print("ProcessPoolExecutor duration:", processpool_duration)