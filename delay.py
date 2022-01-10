import asyncio
import math
from datetime import datetime


async def print_delay(array: list):
    for i, x in enumerate(array):
        await asyncio.sleep(math.pow(2, i))
        print(datetime.now())
        print(x)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(print_delay(["a", "b", "c", "d", "e"]))

