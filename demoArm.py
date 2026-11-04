# Demo-01: How to turn on DBD Stepper Driver
# 示例-01：如何使能DBD步进电机驱动器


from DBDynamics import Ant

m = Ant('/dev/ttyUSB0')  # or COM2 COM3
motor_id = 1  # 目标驱动器的编号
m.setPowerOn(1)
m.setAccTime(1, 500)
m.setAccTime(2, 500)
m.setTargetVelocity(2, 25)
for i in range(0, 3):
    m.setTargetPosition(1, 200000)
    m.setTargetPosition(2, 50000)
    m.waitTargetPositionReached(1)
    m.setTargetPosition(1, 0)
    m.setTargetPosition(2, 0)
    m.waitTargetPositionReached(1)
m.stop()  # 释放接口资源

# Note: when turn on stepper driver, the motor is controlled by driver, otherwise, the motor is free to run.
# 注意：当使能驱动器后，电机受驱动器控制，否则电机可自由转动
