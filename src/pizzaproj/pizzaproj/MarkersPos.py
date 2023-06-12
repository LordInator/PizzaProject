import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose
from std_msgs.msg import String
from tf2_ros.buffer import Buffer
from tf2_ros.transform_listener import TransformListener
from ros2_aruco_interfaces.msg import ArucoMarkers
from geometry_msgs.msg import PoseArray, TransformStamped

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('pizzapos')
        self.publisher_ = self.create_publisher(String, 'MarkNode', 10)
        timer_period = 0.5  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World' 
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

# import rclpy
# from rclpy.node import Node
# from tf2_ros import Buffer
# from std_msgs.msg import String

# class PizzaPose(Node):
#     def __init__(self):
#         super().__init__('pizzapos')
#         self.publisher_ = self.create_publisher(String, 'ArucoPoses', 10)
#         timer_period = 0.5  # seconds
#         self.timer = self.create_timer(timer_period, self.arucocallback)

#     def arucocallback(self):
#         msg = String()
#         msg.data = 'Hi'
#         self.publisher_.publish(msg)
#         self.get_logger.info('This is msg : "%s"' % msg.data)
#         msg = self.tf_buffer.lookupTransform('map','aruco_1', rclpy.time.Time())
#         self.publisher_.publish(msg)
#         self.get_logger().info('Publishing: "%s"' % msg.data)

        

# def main(args=None):
#     rclpy.init(args=args)
#     pizzapos = PizzaPose()
#     rclpy.spin(pizzapos)

#     pizzapos.destroy_node()
#     rclpy.shutdown()


# if __name__ == '__main__':
#     main()
