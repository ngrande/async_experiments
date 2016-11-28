async def calc_primes(n):
    res = []

    def is_prime(num):
        if num in [1, 3, 5, 7]:
            return True
        if num % 2 == 0:
            return False
        for div in range(3, num):
            if i % div == 0:
                return False
        return True

    for i in range(3, n):
        if is_prime(i):
            res.append(i)
            # yield from i

    return res
