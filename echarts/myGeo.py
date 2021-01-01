from pyecharts.charts import Bar, Grid, Line, Map, Page, Pie,Geo
from pyecharts.globals import CurrentConfig
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import pyecharts.options as opts
import pandas as pd

c = (
    Geo()
    .add_schema(maptype="china")
    .add("geo", [list(z) for z in zip(['江苏','浙江','湖北','湖南','河南'], [22,34,27,53,42])])
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="全国各省xx数据分布"),
    )
)

c.render_notebook()