# Demo-11: How to run sync positon mode
# 示例-11：如何设置同步位置模式


from DBDynamics import Ant

m = Ant('/dev/ttyUSB0')  # or m = Ant('COM3') , for windows user
motor_id = 1  # 目标驱动器的编号
m.setPowerOn(motor_id)
m.setSyncPositionMode(motor_id)  # 设置同步位置模式
m.setSyncTargetPosition(motor_id, -105000)  # 设置同步目标位置
m.setSyncRun()  # 设置同步运行

m.stop()  # 释放接口资源

# Note: when turn on stepper driver, the motor is controlled by driver, otherwise, the motor is free to run.
# 注意：当使能驱动器后，电机受驱动器控制，否则电机可自由转动
