from launch import LaunchDescription  # Launch dosyaları için temel sınıf
from launch_ros.parameter_descriptions import ParameterValue  # ROS 2 parametre değerleri için
from launch_ros.actions import Node  # ROS 2 düğümlerini (node) başlatmak için
from launch.substitutions import Command  # Komut satırı ile parametre oluşturmayı sağlar

import os  # Dosya işlemleri için
from ament_index_python.packages import get_package_share_path  # Paketlerin yolunu almak için

########################################

def generate_launch_description():
    # URDF dosyasının bulunduğu yolu belirle
    urdf_path = os.path.join(get_package_share_path('my_robot_description'), 'urdf', 'my_robot.urdf')
    rviz_config_path = os.path.join(get_package_share_path('my_robot_description'), 'rviz', 'urdf_config.rviz')
    
    # URDF dosyasını xacro kullanarak işleyip robot tanımı olarak ayarla
    robot_description = ParameterValue(Command([urdf_path]), value_type=str)
    
    # robot_state_publisher düğümünü başlat (Robotun eklem ve bağlantı bilgilerini yayınlar)
    robot_state_publisher_node = Node(
        package="robot_state_publisher",  # Kullanılacak paket adı
        executable="robot_state_publisher",  # Çalıştırılacak yürütülebilir dosya adı
        parameters=[{'robot_description': robot_description}]  # Robot tanımı parametre olarak veriliyor
    )

    # joint_state_publisher_gui düğümünü başlat (Eklemleri GUI üzerinden değiştirme aracı)
    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",  # Kullanılacak paket
        executable="joint_state_publisher_gui"  # Çalıştırılacak dosya
    )

    # rviz2 düğümünü başlat (Robotu 3D olarak görselleştirmek için kullanılır)
    rviz2_node = Node(
        package="rviz2",  # Kullanılacak paket
        executable="rviz2",  # Çalıştırılacak dosya
        arguments=['-d', rviz_config_path] # belirttiğim path de argümanlarım bulunuyor.
    )

    # LaunchDescription nesnesi oluşturarak düğümleri başlat
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node
    ])
