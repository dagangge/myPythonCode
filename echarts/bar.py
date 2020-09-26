from pyecharts.charts import Bar
from pyecharts import options as opts

bar=Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A",[5, 20, 36, 10, 75, 90])
bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题",subtitle="副标题"))
bar.render("echarts\myBar.html")