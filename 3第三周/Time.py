import time
from datetime import datetime,timedelta
t=time.gmtime()
print(time.strftime("%Y-%m-%d %H:%M:%S",t))

data_els = []
today_ele =datetime.now().date()
data_els.append(['今天', datetime.now().date()])
data_els.append(['昨天', today_ele - timedelta(days=1)])
data_els.append(['近7天', today_ele - timedelta(days=7)])
data_els.append(['近30天', today_ele - timedelta(days=7)])
selected = " "
select_ele=""
for item in data_els:
    option_ele = """<option value="%s" %s>%s</option> """ % (item[1], selected, item[0])
    select_ele += option_ele
print(select_ele)