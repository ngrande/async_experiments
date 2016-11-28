#!/usr/bin/env python3

import asyncio
import time
import ipaddress
import random
import prime


def measure_time(func):
    async def wrapper(*params):
        start = time.monotonic()
        res = await func(params)
        end = time.monotonic()
        duration = float(end - start)
        return (res, duration)
    return wrapper


@measure_time
async def ping(ip):
    # await asyncio.sleep(random.randint(1, 10), loop=loop)
    res = await prime.calc_primes(random.randint(5, 22222))
    return False

async def print_ping(ip):
    responding, duration = await ping(ip)
    print("IP: %s - %s [%f]" % (ip, responding, duration))


def main(ip_range):
    global loop
    loop = asyncio.get_event_loop()
    res = []
    tasks = []
    for ip in ip_range:
        ip_addr = ipaddress.ip_address(ip)
        tasks.append(asyncio.ensure_future(print_ping(ip)))
    loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()

if __name__ == '__main__':
    main(range(0, 100000))
    # loop.run_until_complete(main(loop, range(0, 10000)))
