import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ibrahim/Ros_Egitim/Projeler/Turtlesim_Hedef_Konuma_Git/turtlesim_ws/install/turtlesim_py_pkg'
