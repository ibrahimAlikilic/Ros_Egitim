import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ibrahim/Ros_Egitim/Projeler/Dunya_Modelleme/turtlebot3_ws/install/turtlebot3_example'
