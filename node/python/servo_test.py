#!/usr/bin/env python
import rospy
from std_msgs.msg import Int8
import time
def talker():
    time1 = time.time()
    pub = rospy.Publisher('servo', Int8, queue_size=10)
    rospy.init_node('servotest', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        time2 = time.time()
        time3 = time2 - time1
        value = Int8()
        if (time3 > 15):
            value.data = 1
        else:
            value.data = 0
        pub.publish(value)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



