from DBDynamics import Ant

m = Ant('/dev/ttyUSB0')  # or COM2 COM3
currentID = 1
targetID = 3
m.changeID(id=currentID, value=targetID)
m.stop()