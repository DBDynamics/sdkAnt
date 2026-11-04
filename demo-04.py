# Demo-04: How to set DBD Stepper Driver working at Homing Mode
# 示例-04：如何设置DBD驱动器工作在回零模式

from DBDynamics import Ant

m = Ant('/dev/ttyUSB0')  # or COM2 COM3

motor_id = 1  # 目标驱动器的编号
m.setPowerOn(motor_id)  # 使能
m.setHomingLevel(motor_id, 1)  # 设置回零传感器的触发电平 1/0
m.setHomingDirection(motor_id, 1)  # 设置回零的运动方向 1/-1
m.setTargetVelocity(motor_id, 20)  # 设置回零的运行速度，建议速度慢一些

print("Enter Homing Mode")
m.setHomingMode(motor_id)  # 进入回零模式
m.waitTargetPositionReached(motor_id)  # 等待回零模式完成
print("Homing Done")
m.stop()  # 释放接口资源

# Note: DBD Driver can work at Position Mode, Velocity Mode, Homing Mode and Interpolation Mode.
#       please visit https://roboway.top/products/Ant/#operationmode for details.
# 注意：DBD驱动器可以工作在位置模式，速度模式和回零模式以及插补模式
#       请登录网站 https://roboway.top/products/Ant/#operationmode 查看更加详细的模式信息介绍。
