from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    """
    Launch file that starts the mason_chat publisher and listener on a shared topic name.
    Accepts CLI arguments to override defaults.
    """

    publish_rate_arg = DeclareLaunchArgument(
        'publish_rate',
        default_value='2.0',
        description='Rate at which to publish messages'
    )   

    topic_name_arg = DeclareLaunchArgument(
        'topic_name',
        default_value='launch_chat',
        description='Topic Name of the topic to publish and subscribe to'
    )

    message_prefix_arg = DeclareLaunchArgument(
        'message_prefix',
        default_value='Launch from launch file',
        description='Prefix to add to the message being published'
    )

    # --- substitutions (read at runtime) ---
    publish_rate = LaunchConfiguration('publish_rate')
    topic_name = LaunchConfiguration('topic_name')
    message_prefix = LaunchConfiguration('message_prefix')

    # --- Nodes ---


    talker = Node(
        package = 'my_first_pkg',
        executable = 'hello_node',
        name = 'mason_chat_node',
        output = 'screen',
        parameters = [{'publish_rate': publish_rate, 'message_prefix': message_prefix, 'topic_name' : topic_name,}]
    )

    listener = Node(
        package = 'my_first_pkg',
        executable = 'listener_node',
        name = 'mason_listener_node',
        output = 'screen',
        parameters = [{'topic_name' : topic_name,}]
    )

    return LaunchDescription([publish_rate_arg, topic_name_arg, message_prefix_arg, talker, listener])

