import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ibrahim/Ros_Egitim/Projeler/Lidar/ros2_ws/install/lidar_py_pkg'
