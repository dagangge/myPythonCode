from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.render import make_snapshot
from pyecharts.globals import ThemeType
from snapshot_selenium import snapshot

bar=(
    Bar(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A",[5, 20, 36, 10, 75, 90])
    .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title="主标题",subtitle="副标题"))
)
bar=Bar(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
bar.render("echarts\mybarTheme.html")