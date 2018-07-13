#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64
import math

def talker():
    i=0
    pub = rospy.Publisher('Data', Float64, queue_size=10)
    rospy.init_node('publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        j=math.sin(i)
        pub.publish(j)
        i = i+0.1
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

