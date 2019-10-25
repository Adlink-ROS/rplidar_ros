from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        IncludeLaunchDescription(PythonLaunchDescriptionSource([ThisLaunchFileDir(), '/rplidar.launch.py'])),
        Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            output='screen', 
            arguments=['0', '0', '0', '0', '0', '0', 'odom', 'base_link']
            ),
        Node(
            package='tf2_ros',
            node_executable='static_transform_publisher',
            output='screen',
            arguments=['0', '0', '0', '0', '0', '0', 'base_link', 'laser_frame']
            ),
        Node(
            package='rviz2',
            node_executable='rviz2',
            output='screen',
            arguments=['-d', [ThisLaunchFileDir(), '/../rviz/rplidar.rviz']],
        )
    ])
