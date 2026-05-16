#!/bin/bash
#Launch publisher and subscriber nodes with cleanup hand

cleanup(){
    echo "Restarting ROS2 daemon to clean up before shutting down"
    ros2 daemon stop
    sleep 1
    ros2 daemon start
    echo "Terminating all ROS2-related processes"
    kill 0
    exit
}

trap 'cleanup' SIGINT #FOR CONTROL C

#Launch the publisher node
ros2 run ros2_fundamentals_examples py_minimal_publisher.py &

sleep 2

#aunch the subscriber node 
ros2 run ros2_fundamentals_examples py_minimal_subscriber.py