import time

from DBDynamics import Ant

m = Ant('/dev/ttyUSB0')  # or COM2 COM3
m.setPowerOn(1)
m.setTargetVelocity(1, 50)
m.setAccTime(1, 500)
m.setKeepingCurrent(1, 200)
m.setRunningCurrent(1, 500)


def f_90():
    m.setTargetPosition(1, 12500)
    m.waitTargetPositionReached(1)
    m.setTargetPosition(1, 0)
    m.waitTargetPositionReached(1)


def b_90():
    m.setTargetPosition(1, -12500)
    m.waitTargetPositionReached(1)
    m.setTargetPosition(1, 0)
    m.waitTargetPositionReached(1)


def set0():
    m.setHomingDirection(1, 1)
    m.setTargetVelocity(1, 50)
    m.setHomingLevel(1, 1)
    m.setHomingMode(1)
    time.sleep(1)
    m.waitTargetPositionReached(1)


set0()
f_90()
b_90()
m.stop()
