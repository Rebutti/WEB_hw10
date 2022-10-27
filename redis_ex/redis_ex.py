import redis
from redis_lru import RedisLRU
import timeit

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
@cache
def fibonacci_cache(n):
    if n <= 0:
            return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_cache(n-1)+fibonacci_cache(n-2)

def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)


@cache
def recur_factorial_cache(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial_cache(n-1)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    a = recur_factorial(600)
    print(f'Duration: {timeit.default_timer() - start_time}')
    print(a)
    
    start_time = timeit.default_timer()
    a = recur_factorial_cache(600)
    print(f'Duration: {timeit.default_timer() - start_time}')
    print(a)