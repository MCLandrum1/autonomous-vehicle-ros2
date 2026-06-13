from platform import node

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class MasonListenerNode(Node):
    def __init__(self):
        super().__init__('mason_listener_node')
        self.subscription_ = self.create_subscription(
            String,
            'mason_chat',
            self.message_callback,
            10
        )
        self.subscription_  # prevent unused variable warning
        self.get_logger().info('MasonListenerNode has been started.')
        self.received_count = 0
    def message_callback(self, msg):
        self.received_count += 1
        self.get_logger().info(f'[#{self.received_count} ] Received "{msg.data}"')
    
def main(args=None):
    rclpy.init(args=args)
    node = MasonListenerNode()
    try:
        rclpy.spin(node)
        
    except KeyboardInterrupt:
            pass
    finally:    
            node.destroy_node()
            rclpy.shutdown()
if __name__ == '__main__':
    main()
    