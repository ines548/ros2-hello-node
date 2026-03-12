

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import random

class TemperaturePublisher(Node):
    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher_ = self.create_publisher(Float64, 'temperature', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        temp = 20.0 + random.uniform(-0.5, 0.5)
        msg = Float64()
        msg.data = temp
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing temperature: {temp:.2f} °C")

def main(args=None):
    rclpy.init(args=args)
    node = TemperaturePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
