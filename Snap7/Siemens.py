import struct
import time
import snap7
import datetime

# plc	        rack	slot
# s7-200smart	0	1
# s7-300	    0	2
# s7-400/WIN AC	见硬件组态	见硬件组态
# s7-1200/1500	0	0/1
def plc_connect(ip, rack=0, slot=0):
    client = snap7.client.Client()
    client.connect(ip, rack, slot)
    return client


def plc_con_close(client):
    client.disconnect()


def test_mk10_1(client):
    area = snap7.types.S7AreaDB
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
    area = snap7.types.areas.MK
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
    client_fd = plc_connect('10.0.69.79')
    test_mk10_1(client_fd)
    plc_con_close(client_fd)
