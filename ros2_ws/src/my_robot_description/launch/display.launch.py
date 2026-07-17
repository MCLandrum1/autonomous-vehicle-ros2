import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():
    """Launch robot_state_publisher, joint_state_publisher_gui, and RViz."""

    pkg_share = get_package_share_directory('my_robot_description')
    default_urdf_path = os.path.join(pkg_share, 'urdf', 'my_robot.urdf')
    rviz_config = os.path.join(pkg_share, 'rviz', 'display.rviz')

    urdf_arg = DeclareLaunchArgument(
        name='urdf',
        default_value=default_urdf_path,
        description='Path to the URDF file'
    )

    robot_description = ParameterValue(
        Command(['cat ', LaunchConfiguration('urdf')]),
        value_type=str
    )

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_description}]
    )

    joint_state_publisher_gui = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        output='screen'
    )

        # RViz2 with pre-loaded config
    rviz_config = os.path.join(pkg_share, 'rviz', 'display.rviz')
    rviz = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config],
    )
    return LaunchDescription([
        urdf_arg,
        robot_state_publisher,
        joint_state_publisher_gui,
        rviz,
    ])