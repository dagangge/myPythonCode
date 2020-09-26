# encoding: utf-8 
import paho.mqtt.client as mqtt
 
HOST = "192.168.55.181"
PORT = 8887
 
def test():
    client_id = "55181"
    client = mqtt.Client(client_id=client_id)
    client.connect(HOST, PORT, 60)
    client.publish("hs000V/state","hello liefyuan",2) # 发布一个主题为'chat',内容为‘hello liefyuan’的信息
    #print("被调用")
    client.loop_forever()
    
 
if __name__ == '__main__':
    test()