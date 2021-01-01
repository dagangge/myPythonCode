# -*- coding:utf-8 -*-
import io,sys
import asyncio

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
async def func1():
    print(f'1快来搞我吧！')
    await asyncio.sleep(2)
    print(2)
async def func2():
    print(f'3')
    await asyncio.sleep(2)
    print(4)

tasks=[
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
    # asyncio.create_task(func1()),
    # asyncio.create_task(func2())
]

loop=asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))