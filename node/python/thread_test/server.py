#!/usr/bin/env python
import rospy
from smartcar.srv import addtwoints
import thread
import time
def addition(a,b):
    while 1:
        s=a+b
        print s
        time.sleep(2)
        
def handle_add_two_ints(req):#process the data from client
    dic = {}
    a=req.a
    b=req.b
    thread.start_new_thread(addition,(a,b)) 
    thread_id=thread.get_ident()
    dic.setdefault(a,thread_id)
    print dic
    
def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    rospy.Service('add_two_ints', addtwoints, handle_add_two_ints)
    
    print "Ready to add two ints."
    rospy.spin()

if __name__ == "__main__":
     add_two_ints_server()



