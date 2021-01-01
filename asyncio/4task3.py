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
    tasklist=[
        func1(),
        func1()
    ]
    print(f'fun2结束')
    done,pending=await asyncio.wait(tasklist,timeout=None)
    print(done,pending)

asyncio.run(func2())


# 协程函数内部代码
# fun2结束
# 1快来搞我吧！
# 1快来搞我吧！
# 1快来搞我吧！
# 2end
# 2end
# 2end
# {<Task finished coro=<func1() done, defined at d:\Source\myPythonCode\asyncio\4task2.py:6> result='返回值'>, <Task finished coro=<func1() done, defined at d:\Source\myPythonCode\asyncio\4task2.py:6> result='返回值'>, <Task finished coro=<func1() done, defined at d:\Source\myPythonCode\asyncio\4task2.py:6> result='返回值'>}