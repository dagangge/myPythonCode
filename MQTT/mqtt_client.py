# -*- coding: utf-8 -*- 
import paho.mqtt.client as mqtt
from configparser import ConfigParser
import time
 

config=ConfigParser()
config.read("config.ini",encoding="utf-8")
MQTTB_HOST=config.get("mqttbroker","mqttb_host")
MQTTB_PORT=config.getint("mqttbroker","mqttb_port")
HOSPITALID=config.get("section","HospitalID")



# rc:
# 0: 连接成功
# 1: 连接失败-不正确的协议版本
# 2: 连接失败-无效的客户端标识符
# 3: 连接失败-服务器不可用
# 4: 连接失败-错误的用户名或密码
# 5: 连接失败-未授权
# 6-255: 未定义.
def on_connect(client, userdata, flags, rc):
        client.subscribe(HOSPITALID+'/Server/Time',qos=0)
        print("Connection returned " + str(rc))

# 当客户端与Broker断开时调用
def on_disconnect(client, userdata, rc):
        time.sleep(1)
        client.connect(MQTTB_HOST, MQTTB_PORT, 60)
 
 
# 当使用publish()发送的消息已经完成传输到代理时调用
def on_publish(client, userdata, mid):
        pass 
    
# 消息处理函数
# “msg”变量是一个MQTT消息描述所有消息特征
def on_message_come(client, userdata, msg): 
    print(msg.topic + " " + ":" + str(msg.payload))
 
 
# 当Broker响应订阅请求时调用
def on_subscribe(client, userdata, mid, granted_qos):
        pass

# 当Broker响应取消订阅请求时调用
def on_unsubscribe(client, userdata, mid):
        pass
        

def MQTTClient():
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_disconnect=on_disconnect
        client.on_message=on_message_come
        client.connect(MQTTB_HOST, MQTTB_PORT, 60)
        client.publish("/test/server", "Hello Python!", 1)
        
        client.loop_start()
        return client
if __name__ == '__main__':
        client.on_connect = on_connect
        client.on_disconnect=on_disconnect
        client.on_message=on_message_come
        client.on_subscribe=on_subscribe
        client.on_subscribe=on_subscribe
        client.connect(MQTTB_HOST, MQTTB_PORT, 60)
        client.publish("/test/server", "Hello Python!", 1)
        
        client.loop_start()
        client._state=mqtt.mqtt_cs_connected