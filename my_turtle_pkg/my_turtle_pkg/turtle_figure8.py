import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math


class TurtleFigure8(Node):

    def __init__(self):
        super().__init__('turtle_figure8')

        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.timer = self.create_timer(
            0.1,
            self.move_turtle
        )

        self.t = 0.0

    def move_turtle(self):
        msg = Twist()

        msg.linear.x = 2.0
        msg.angular.z = 2.0 * math.sin(self.t)

        self.publisher.publish(msg)

        self.t += 0.1


def main(args=None):
    rclpy.init(args=args)

    node = TurtleFigure8()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
