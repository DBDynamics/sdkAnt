# 扫描在线设备
from DBDynamics import Ant
m = Ant('/dev/ttyUSB0')  # or COM2 COM3
m.scanDevices()
m.stop()