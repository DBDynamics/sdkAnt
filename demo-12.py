# Demo-12: How to get actual position
# 示例-12：如何获取当前的电机位置信息


from DBDynamics import Ant
import time

m = Ant('/dev/ttyUSB0')  # or m = Ant('COM3') , for windows user
motor_id = 1  # 目标驱动器的编号
for i in range(0, 10):
    time.sleep(0.1)
    print(m.getActualPosition(motor_id)) # 获取并打印当前位置

m.stop()  # 释放接口资源

# Note: when turn on stepper driver, the motor is controlled by driver, otherwise, the motor is free to run.
# 注意：当使能驱动器后，电机受驱动器控制，否则电机可自由转动
