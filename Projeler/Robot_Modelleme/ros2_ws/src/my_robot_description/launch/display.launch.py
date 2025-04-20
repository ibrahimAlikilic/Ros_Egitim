import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo, ExecuteProcess, TimerAction
#from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command
import launch_ros.actions
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # my_robot paketinin paylaşım dizinini al
    pkgPath = get_package_share_directory('my_robot_description')
    print(f"PKGPATH : {pkgPath}")

    # main.xacro dosyasının yolunu belirt
    urdfModelPath = os.path.join(pkgPath, 'urdf', 'main.xacro')

    # xacro dosyasını çözümle ve robot_description parametresine aktar
    robot_desc = Command(['xacro ', urdfModelPath]) # Yol belirttiğinden arada bolşuk olmalı
    params = {'robot_description': robot_desc}

    # Gazebo Classic'i başlatmak için ExecuteProcess kullanıyoruz.
    # gazebo_process = ExecuteProcess(
    #     cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
    #     output='screen'
    # )

    # spawn_entity.py ile robotu Gazebo'ya ekleyecek node'u TimerAction ile 5 saniye geciktiriyoruz.
    # spawn_entity_node = TimerAction(
    #     period=5.0,
    #     actions=[
    #         launch_ros.actions.Node(
    #             package='gazebo_ros',
    #             executable='spawn_entity.py',
    #             arguments=[
    #                 '-entity', 'my_robot',
    #                 '-topic', 'robot_description'
    #             ],
    #             output='screen'
    #         )
    #     ]
    # )

    # robot_state_publisher node
    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name="robot_state_publisher",
        output='screen',
        parameters=[params]
    )

    # joint_state_publisher node
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        output='screen',
        parameters=[params]
    )

    # RViz node
    rviz_node = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        parameters=[params],
        arguments=['-d', os.path.join(pkgPath, 'rviz', 'robot_config.rviz')]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            name="model", default_value=urdfModelPath, description="URDF model xacro file"
        ),
        # gazebo_process,
        # spawn_entity_node,
        LogInfo(msg="Gazebo Classic and ROS 2 integration launched successfully."),
        robot_state_publisher_node,
        joint_state_publisher_node,
        rviz_node
    ])