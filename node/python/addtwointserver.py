#!/usr/bin/env python
import rospy
from base_control.srv import addtwoints
def handle_add_two_ints(req):#process the data from client
    while 1:
         s=req.a + req.b
         return s
         print s
    
def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    rospy.Service('add_two_ints', addtwoints, handle_add_two_ints)
    
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
     add_two_ints_server()


