#!/usr/bin/env python
import sys
import rospy
from base_control.srv import addtwoints
import time

def add_two_ints_client(x, y):
    rospy.wait_for_service('add_two_ints')
    try:
        add_two_ints = rospy.ServiceProxy('add_two_ints', addtwoints)
        resp1 = add_two_ints(x, y)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]
if __name__ == "__main__":
    rospy.init_node('client')
    x=rospy.get_param('~a')
    y=rospy.get_param('~b')
   
    print "Requesting %s+%s"%(x, y)
    start = time.time()
    print " %s"%(add_two_ints_client(x, y))
    stop = time.time()
    interval = stop-start
    print 'interval',interval


    

