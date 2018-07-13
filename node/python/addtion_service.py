#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 17:17:25 2017

@author: ros
"""


import rospy #导入模块
from smartcar.msg import addtion

def talker():#定义发布者函数
    pub = rospy.Publisher('add_topic',addtion, queue_size=10)#定义发布的消息类型以及发布到那个主题
    rospy.init_node('add_service', anonymous=True)#创建发布节点命名为
   
    while not rospy.is_shutdown():#rospy没有停止时，进入循环发布具体消息
        value=addtion()#定义消息

        value.x=2
        value.y=3
        
        pub.publish(value)#发布消息到主题，此处为隐式调用publish
       

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

