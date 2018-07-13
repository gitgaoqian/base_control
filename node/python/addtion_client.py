#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 19:12:18 2017

@author: ros
"""


import rospy
from smartcar.msg import addtion
import time
def callback(data):
    a=time.time()
    result=data.x+data.y
    b=time.time()
    print 'interval', b-a
    print ("%f"%result)
#callback处理的是从发布者得到的消息，这里括号里的参数

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('add_client', anonymous=True)#命名订阅节点

    rospy.Subscriber("add_topic", addtion, callback)#定义订阅消息类型为std_msgs.msg String的主题，
#关于callback的参数：callback (fn(msg, cb_args)) - function to call ( fn(data)) when data is received. If callback_args is set, the function must accept the callback_args as a second argument, i.e. fn(data, callback_args). NOTE: Additional callbacks can be added using add_callback().

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
