#encoding=utf-8
from pyecharts import Liquid
liquid =Liquid("水球图示例")
arg = 1
if arg == 1:
    liquid.add("Liquid", [0.6])
    liquid.show_config()
    liquid.render()
else:
    liquid.add("Liquid", [0.6, 0.5, 0.4, 0.3], is_liquid_animation=False, shape='diamond')
    liquid.show_config()
    liquid.render()
