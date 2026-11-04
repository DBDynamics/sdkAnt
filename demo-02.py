# Demo-02: How to turn off DBD Stepper Driver
# 示例-02：如何失能DBD步进电机驱动器


from DBDynamics import Ant

m = Ant('/dev/ttyUSB0')  # or COM2 COM3
motor_id = 1  # 目标驱动器的编号
m.setPowerOff(motor_id)

m.stop()  # 释放接口资源

# Note: when turn on stepper driver, the motor is controlled by driver, otherwise, the motor is free to run.
# 注意：当使能驱动器后，电机受驱动器控制，否则电机可自由转动
