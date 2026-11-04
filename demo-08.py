# 示例-08：让两台电机同时运动, 工作在位置模式
from DBDynamics import Ant
import time

m = Ant('/dev/ttyUSB0')  # or COM2 COM3
motorA_id = 1  # A驱动器的编号
motorB_id = 2  # B驱动器的编号

m.setPowerOn(motorA_id)
m.setPowerOn(motorB_id)

m.setPositionMode(motorA_id)  # 设置运行模式
m.setPositionMode(motorB_id)  # 设置运行模式
m.setTargetVelocity(motorA_id, 100)  # 设置目标速度
m.setTargetVelocity(motorB_id, 100)  # 设置目标速度
m.setAccTime(motorA_id, 500)  # 设置加速时间
m.setAccTime(motorB_id, 500)  # 设置加速时间

pos_a = 50000 * 1  # 目标位置a 正一圈
pos_b = 50000 * -1  # 目标位置b 负一圈

for loop in range(0, 3):  # 循环3次
    m.setTargetPosition(motorA_id, pos_a)  # 设置目标位置a
    m.setTargetPosition(motorB_id, pos_b)  # 设置目标位置a
    time.sleep(0.5)
    m.waitTargetPositionReached(motorA_id)  # 等待到达目标位置
    m.waitTargetPositionReached(motorB_id)  # 等待到达目标位置

    m.setTargetPosition(motorA_id, pos_b)  # 设置目标位置b
    m.setTargetPosition(motorB_id, pos_a)  # 设置目标位置b
    time.sleep(0.5)
    m.waitTargetPositionReached(motorA_id)  # 等待到达目标位置
    m.waitTargetPositionReached(motorB_id)  # 等待到达目标位置


m.stop()  # 释放接口资源

# Note: when turn on stepper driver, the motor is controlled by driver, otherwise, the motor is free to run.
# 注意：当使能驱动器后，电机受驱动器控制，否则电机可自由转动
