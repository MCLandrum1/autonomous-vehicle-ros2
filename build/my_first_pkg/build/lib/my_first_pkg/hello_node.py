import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MasonChatNode(Node):
    def __init__(self):
        super().__init__('mason_chat_node')
        # -- Declare parameters with defaults --
        self.declare_parameter('publish_rate', 1.0)
        self.declare_parameter('message_prefix', 'Hello, from mason !!!')
        self.declare_parameter('topic_name', 'mason_chat')

        # --- Read parameter values ---

        publish_rate = self.get_parameter('publish_rate').value
        self.message_prefix = self.get_parameter('message_prefix').value
        topic_name = self.get_parameter('topic_name').value

        # -- Validate ---

        if publish_rate <=0:
            self.get_logger().warn('Publish_rate must be positive. got {publish_rate}. Using default value of 1.0 Hz.')
            raise ValueError('Publish_rate must be positive.')
        
        # -- User parameters ---
        timer_period = 1.0 / publish_rate
        self.publisher_ = self.create_publisher(String, topic_name, 10)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter = 0

        self.get_logger().info(
            f'MasonChatNode started with publish_rate: {publish_rate} Hz, message_prefix: "{self.message_prefix}", topic_name: "{topic_name}"'
        )

    def timer_callback(self):
        msg = String()
        msg.data = f'{self.message_prefix} - msg #{self.counter}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.counter += 1



def main(args=None):
    rclpy.init(args=args)
    node = MasonChatNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
