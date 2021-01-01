import requests
import asyncio
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


async def fetch(url):
    print(f'发送请求：{url}')
    loop=asyncio.get_event_loop()
    future=loop.run_in_executor(None,requests.get,url)
    response=await future
    print(f'请求完成：{url}')
    file_name = url.rsplit('_')[-1]
    with open(file_name, mode='wb') as file_object:
        file_object.write(response.content)

if __name__ == "__main__":
    urllist = [
            'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
            'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
            'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
        ]
    tasks = [fetch(url) for url in urllist]

    loop =asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
