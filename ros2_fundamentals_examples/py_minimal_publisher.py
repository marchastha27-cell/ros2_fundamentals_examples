#! /usr/bin/env python3

"""
Description:
  this ros2 node periodically publishes hello world messages to topic
-----
Publishing Topics:
  the channel containing the hello world  messgaes
  /py_example_topic - std_msgs/String

Subsciption Topics:
  none
-----
Author: Astha
Date:14/05/2026

"""
import rclpy #imports the ros2 client library for python
from rclpy.node import Node #imports the Node class from the rclpy library

from std_msgs.msg import String #imports the String message type from the std_msgs package

class MinimalPyPublisher(Node):
    """
    Create a minimal publisher node .

    """
    def __init__(self):
        """
        Create a custom node with a name 
        """
        #Inirialize the node with the name 'minimal_py_publisher'
        super().__init__('minimal_py_publisher')

        #Create a publisher on the topic with a queue size of ten messages 
        self.publisher_1 = self.create_publisher(String, '/py_example_topic', 10)

        #Create a timer with a period of 0.5  seconds to trigger publushing of messages 
        timer_period = 0.5 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        
        #Initialize a counter variable for message content 
        self.i=0
    def timer_callback(self):
        """
        Callback function executed periodically by the timer that is every half second
        """
        msg = String()
        #Set the msg data with a counter
        msg.data = 'Hello World: %d'% self.i

        #Publish the message you created above to a topic
        self.publisher_1.publish(msg)
        
        #Log a message  indicating the message has been published
        self.get_logger().info('Publishing:"%s"' %msg.data)

        self.i +=1 #Increment the counter for the next message

def main(args=None):
        """
        Main function to initialize the ROS2 node and start the publisher

        Args:
            args(List, optional): Command line arguments. Defaults to None.
        """
        rclpy.init(args=args)

        #Create an instance of the minimal publisher node
        minimal_py_publisher = MinimalPyPublisher()

        rclpy.spin(minimal_py_publisher)

        #Destroy the node explicitly
        minimal_py_publisher.destroy_node()

        #Shutdown Ros2 communications
        rclpy.shutdown()
        
if __name__ == '__main__':
#Execute the main function if the script is run directly
 main()

        