"""
Bu dosya, ROS 2'de bir launch (başlatma) dosyası olarak kullanılır.
Bu launch dosyası, aşağıdaki bileşenleri başlatır:
1. robot_state_publisher: Robotun eklem (joint) ve bağlantı (link) bilgilerini yayınlar.
2. joint_state_publisher_gui: Robotun eklem hareketlerini GUI üzerinden değiştirmek için kullanılır.
3. rviz2: Robotun görselleştirilmesini sağlamak için RViz 2 başlatılır.
"""

from launch import LaunchDescription  # Launch dosyaları için temel sınıf
from launch_ros.parameter_descriptions import ParameterValue  # ROS 2 parametre değerleri için
from launch_ros.actions import Node  # ROS 2 düğümlerini (node) başlatmak için
from launch.substitutions import Command  # Komut satırı ile parametre oluşturmayı sağlar

import os  # Dosya işlemleri için
from ament_index_python.packages import get_package_share_path  # Paketlerin yolunu almak için

########################################

def generate_launch_description():
    """
    ROS 2'de başlatılacak düğümleri tanımlayan fonksiyon.
    Bu fonksiyon, robotun durum yayıncısını (robot_state_publisher),
    eklem durumlarını GUI ile değiştirmeye izin veren aracı
    (joint_state_publisher_gui) ve RViz2'yi başlatır.
    """

    # URDF dosyasının bulunduğu yolu belirle
    urdf_path = os.path.join(get_package_share_path('simple_robot_description'), 'urdf', 'simple_robot.urdf')
    
    # URDF dosyasını xacro kullanarak işleyip robot tanımı olarak ayarla
    robot_description = ParameterValue(Command(['xacro', urdf_path]), value_type=str)
    
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
        executable="rviz2"  # Çalıştırılacak dosya
    )

    # LaunchDescription nesnesi oluşturarak düğümleri başlat
    return LaunchDescription([
        robot_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node
    ])
