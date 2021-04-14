# -*- coding:utf-8 -*-
import json
import io,sys
import asyncio

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

list_data = [
    {'id': 1, 'name': '体育0', 'pid': 0},  # pid为0表示顶级
    {'id': 2, 'name': '体育1', 'pid': 1},  # pid的值等于id，则表示是那个元素的子级
    {'id': 3, 'name': '体育2', 'pid': 1},
    {'id': 4, 'name': '体育3', 'pid': 2},
    {'id': 5, 'name': '体育4', 'pid': 2},
    {'id': 6, 'name': '体育5', 'pid': 5},
    {'id': 7, 'name': '体育6', 'pid': 5},
    {'id': 8, 'name': '体育7', 'pid': 5},
    {'id': 8, 'name': '体育7', 'pid': 11},
]


def get_list(pid):
    data = []

    for x in list_data:
        if x['pid'] == pid:
            next_pid = x['id']
            x['sons'] = get_list(next_pid)
            data.append(x)

    return data


if __name__ == '__main__':
    print(json.dumps(get_list(0), ensure_ascii=False))