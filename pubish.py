#!/usr/bin/env python


import rospy
from geometry_msgs.msg import Twist
import time
start_time=stop_time=time.time()
interval=0
def talker():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        twist=Twist()
        vx=cmd_vel()
        twist.linear.x=vx
        twist.linear.y=0
        twist.linear.z=0
        pub.publish(twist)
        rate.sleep()
        
def cmd_vel():
    global start_time
    global stop_time
    interval=stop_time-start_time
    if interval<5:
        value=0.00
    if 5<interval<11:
        value=0.03*(interval-1)
    else:
        value=0.3
    stop_time=time.time()
    return value
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
