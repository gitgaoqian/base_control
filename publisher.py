#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
from neu_wgg.msg import env
import time
import dynamic_reconfigure.client
cur_rate = 10.0
def talker():
    global cur_rate
    pub = rospy.Publisher('chatter', env, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    server_ip = "192.168.1.100"
    rospy.set_param("img_pub_rate",10)
    client = dynamic_reconfigure.client.Client("/camera/left/image/compressed")
    info = client.get_configuration()
    params = {"jpeg_quality":10}
    client.update_configuration(params)
    print info
    while not rospy.is_shutdown():
        img_pub_rate = rospy.get_param("img_pub_rate")
        rate = rospy.Rate(img_pub_rate)
        value = env()
        value.atmo = 1
        value.temp = 2
        value.hum = 3
        pub.publish(value)
        # rate.sleep()
        time.sleep(2)
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
