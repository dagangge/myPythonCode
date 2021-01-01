# -*- coding:utf-8 -*-
import io,sys
import asyncio

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
async def func1():
    print(f'1快来搞我吧！')
    response= await asyncio.sleep(2)
    print(f'IO执行结果：{response}')

result=func1()
asyncio.run(result)