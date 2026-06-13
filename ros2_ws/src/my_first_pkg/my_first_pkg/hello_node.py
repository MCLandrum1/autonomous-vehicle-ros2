import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MasonChatNode(Node):
    def __init__(self):
        super().__init__('mason_chat_node')
        self.publisher_ = self.create_publisher(String, 'mason_chat', 10)
        timer_period = 0.005  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.counter = 0
        self.get_logger().info('MasonChatNode has been started.')

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello i see a obsticle 10meter away!!!- msg {self.counter}'
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
