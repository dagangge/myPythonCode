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
    task1=asyncio.create_task(func1())
    task2=asyncio.create_task(func1())
    print(f'fun2结束')
    ret1 = await task1
    ret2 = await task2
    print(ret1, ret2)

asyncio.run(func2())


# 协程函数内部代码
# fun2结束
# 1快来搞我吧！
# 1快来搞我吧！
# 2end
# 2end
# 返回值 返回值