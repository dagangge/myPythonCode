import struct
import time
import snap7
import datetime


def plc_connect(ip, rack=0, slot=0):
    client = snap7.client.Client()
    client.connect(ip, rack, slot)
    return client


def plc_con_close(client):
    client.disconnect()


def test_mk10_1(client):
    area = snap7.snap7types.S7AreaDB
    dbnumber = 9
    start = 136
    start = 204
    amount = 8
    print(u'初始值')
    mk_data = client.read_area(area, dbnumber, start, amount)
    listdate=list(mk_data)
    # print(struct.unpack('!c', mk_data))
    print(listdate)
    # print(u'置1')
    # client.write_area(area, dbnumber, start, 10)
    # print(u'当前值')
    # mk_cur = client.read_area(area, dbnumber, start, amount)
    # print(struct.unpack('!c', mk_cur))


def test_mk_w201(client):
    area = snap7.snap7types.areas.MK
    dbnumber = 0
    amount = 2
    start = 201
    print(u'初始值')
    mk_data = client.read_area(area, dbnumber, start, amount)
    print(struct.unpack('!h', mk_data))
    print(u'置12')
    client.write_area(area, dbnumber, start, b'')
    print(u'当前值')
    mk_cur = client.read_area(area, dbnumber, start, amount)
    print(struct.unpack('!h', mk_cur))
    time.sleep(3)
    print(u'置3')
    client.write_area(area, dbnumber, start, b'')
    print(u'当前值')
    mk_cur = client.read_area(area, dbnumber, start, amount)
    print(struct.unpack('!h', mk_cur))


if __name__ == "__main__":
    client_fd = plc_connect('192.168.5.1')
    test_mk10_1(client_fd)
    plc_con_close(client_fd)
