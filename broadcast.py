import time

from DBDynamics import Ant

m = Ant('/dev/ttyUSB0')  # or COM2 COM3
m.setPowerOn(1)
m.setPowerOn(119)
m.setAccTime(1, 100)
m.setAccTime(119, 100)
m.setTargetVelocity(1, 200)
m.setTargetVelocity(119, 200)
time.sleep(1)
m.setBroadCastMode(True)
m.setBroadcastPowerOn()
for k in range(0, 11):
    p = -5000 * k
    for i in range(1, 121):
        m.broadcast_position[i] = p
    m.setBroadcastPosition()
    time.sleep(0.5)

for i in range(1, 121):
    m.broadcast_position[i] = 0

    m.setBroadcastPosition()
time.sleep(1)
m.setBroadCastMode(False)
time.sleep(1)
m.stop()
