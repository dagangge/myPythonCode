#pip install pymssql
import pymssql
import pandas as pd

conn=pymssql.connect(host='127.0.0.1',user='sa',password='trace',database='XHCSSD60DB')
if conn:
    print("连接成功！")

cur=conn.cursor()
sql="SELECT DeviceNo, ProgramNo FROM dbo.t_St_Config ORDER BY DeviceNo"
cur.execute(sql)
programs=cur.fetchall()
dfprograms=pd.DataFrame(programs,columns=['DeviceNo','ProgramNo'])
print(dfprograms.groupby(['DeviceNo'])['ProgramNo'].size())

cur.close()
conn.close()
