import time

from DBDynamics import Ant

m = Ant('/dev/ttyUSB0')  # or COM2 COM3
m.setPowerOn(1)
m.setHomingDirection(1, 1)

m.setHomingLevel(1, 1)
m.setTargetVelocity(1, 50)

m.setHomingMode(1)
time.sleep(0.5)
m.waitTargetPositionReached(1)
print("home done!")
m.stop()
