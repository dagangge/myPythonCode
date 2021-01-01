# -*- coding:utf-8 -*-
import io,sys
import asyncio

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
async def func1():
    print('1快来搞我吧！')
    await asyncio.sleep(2)
    print('2end')
    return '返回值'

async def func2():
    print('协程函数内部代码')
    response= await func1()
    print(f'IO执行结果：{response}')
    response2= await func1()
    print(f'IO执行结果：{response2}')

asyncio.run(func2())