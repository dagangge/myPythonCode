import json

# str = '''
# [{
#     "name":"小明",
#     "age":"18"
# }]
# '''
# data=json.loads(str)
# print(data)
# print(type(data))
# print(data[0].get("name"))

str=[{
    "name":"小明",
    "age":"18"
}]
# print(type(str))
# data=json.dumps(str)#转成json字符串
# print(type(data))
# print(data)

# with open("json/123.json","w",encoding="utf-8") as myfile:
#     myfile.write(json.dumps(str,indent=2,ensure_ascii=False))

json.dump(str,open("json/123.json","w",encoding="utf-8"))
data=json.load(open("json/123.json","r",encoding="utf-8")) #从文件里转成python对象list
print(type(data))
print(data)



