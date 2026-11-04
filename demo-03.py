# Demo-03: How to set DBD Stepper Driver working at Position Mode
# 示例-03：如何设置DBD驱动器工作在位置模式，并且在AB两个位置点间反复运行3次。

from DBDynamics import Ant
import time

m = Ant('/dev/ttyUSB0')  # or COM2 COM3

motor_id = 1  # 目标驱动器的编号
m.setPositionMode(motor_id)  # 设置运行模式
m.setTargetVelocity(motor_id, 100)  # 设置目标速度
m.setAccTime(motor_id, 500)  # 设置加速时间
m.setPowerOn(motor_id)  # 使能

pos_a = 50000 * 1  # 目标位置a 正一圈
pos_b = 50000 * -1  # 目标位置b 负一圈

for loop in range(0, 3):  # 循环3次
    m.setTargetPosition(motor_id, pos_a)  # 设置目标位置a
    time.sleep(0.5)
    m.waitTargetPositionReached(motor_id)  # 等待到达目标位置

    m.setTargetPosition(motor_id, pos_b)  # 设置目标位置b
    time.sleep(0.5)
    m.waitTargetPositionReached(motor_id)  # 等待到达目标位置

m.stop()  # 释放接口资源

# Note: DBD Driver can work at Position Mode, Velocity Mode, Homing Mode and Interpolation Mode.
#       please visit https://roboway.top/products/Ant/#operationmode for details.
# 注意：DBD驱动器可以工作在位置模式，速度模式和回零模式以及插补模式
#       请登录网站 https://roboway.top/products/Ant/#operationmode 查看更加详细的模式信息介绍。
