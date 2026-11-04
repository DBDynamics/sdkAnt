# 修改ID编号
from DBDynamics import Ant
m = Ant('/dev/ttyUSB0')  # or COM2 COM3
currentID = 1 #当前编号
targetID = 3 #目标编号
# 将currentID改为targetID
m.changeID(id=currentID, value=targetID)
m.stop()