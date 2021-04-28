from time import sleep
from msedge.selenium_tools import Edge, EdgeOptions

#edge无头浏览器   phantomJs可用，已停止更新
options = EdgeOptions()
options.use_chromium = True

wd = Edge(options = options)
wd.get('https://www.zhipin.com/c101210100-p100122/?page=1&ka=page-1')