from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg = get_package_share_directory('explore_robot_pkg')
    nav2_bringup = get_package_share_directory('nav2_bringup')

    slam = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            get_package_share_directory('slam_toolbox'),
            '/launch/online_async_launch.py'
        ]),
        launch_arguments={
            'slam_params_file': os.path.join(pkg, 'config', 'slam_toolbox.yaml'),
            'use_sim_time': 'true'
        }.items()
    )

    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            nav2_bringup, '/launch/navigation_launch.py'
        ]),
        launch_arguments={
            'params_file': os.path.join(pkg, 'config', 'nav2_params.yaml'),
            'use_sim_time': 'true'
        }.items()
    )

    return LaunchDescription([
        slam,
        nav2,
    ])