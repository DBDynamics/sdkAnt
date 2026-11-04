import time

from DBDynamics import Ant

m = Ant('/dev/ttyUSB0')  # or COM2 COM3
m.setPowerOn(1)

# Start Homing
m.setRunningCurrent(1, 800)
m.setKeepingCurrent(1, 300)
m.setHomingDirection(1, 1)
m.setHomingLevel(1, 1)
m.setTargetVelocity(1, 20)
m.setHomingMode(1)
time.sleep(0.5)
m.waitTargetPositionReached(1)
print("home done!")
for loop in range(0,3):
# while True:
    # for i in range(0, 3):
    # Move to Point A
    m.setTargetVelocity(1, 200)
    m.setAccTime(1, 500)
    m.setTargetPosition(1, -50000 * 2)
    time.sleep(1)
    m.waitTargetPositionReached(1)
    print("Point A Reached!")

    # Move to Point B
    m.setTargetVelocity(1, 100)
    m.setAccTime(1, 1000)
    m.setTargetPosition(1, -50000)
    time.sleep(1)
    m.waitTargetPositionReached(1)
    print("Point B Reached!")

m.setPowerOff(1)
m.stop()
