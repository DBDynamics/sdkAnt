# Demo-01: How to read actual velocity of the stepper motor drive
# 示例-01：如何读取电机驱动的实时速度

from DBDynamics import Ant
import time

m = Ant('/dev/ttyUSB0')  # or Ant('COM2') COM3
motor_id = 1  # 目标驱动器的编号 address for target motor drive
for loop in range(0, 10):
    actual_velocity = m.getActualVelocity(motor_id)
    print(actual_velocity)
    time.sleep(0.1)

m.stop()  # 释放接口资源

# Note: when turn on stepper driver, the motor is controlled by driver, otherwise, the motor is free to run.
# 注意：当使能驱动器后，电机受驱动器控制，否则电机可自由转动
