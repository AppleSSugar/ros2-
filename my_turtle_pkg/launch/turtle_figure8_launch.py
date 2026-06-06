from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_turtle_pkg',
            executable='turtle_figure8',
            name='turtle_figure8_node',
            output='screen'
        )
    ])
