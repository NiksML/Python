
from functools import lru_cache

@lru_cache(maxsize=None)  # Используем lru_cache для кеширования результатов
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Пример использования:
for i in range(20):
    result = fibonacci(i)
    print(result)
