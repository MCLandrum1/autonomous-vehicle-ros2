from platform import node

import rclpy
from rclpy.node import Node
from std_msgs.msg import String




class MasonListenerNode(Node):
    def __init__(self):
        super().__init__('mason_listener_node')


        # -- parameter for topic name 
        self.declare_parameter('topic_name', 'mason_chat')
        topic_name = self.get_parameter('topic_name').value

        self.subscription = self.create_subscription(
            String,
            topic_name,
            self.message_callback,
            10
        )
        
        self.received_count = 0
        self.get_logger().info(f'MasonListenerNode subscribed to topic "{topic_name}"')     



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
    