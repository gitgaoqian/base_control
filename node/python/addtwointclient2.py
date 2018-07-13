#!/usr/bin/env python
import sys
import rospy
from base_control.srv import addtwoints

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
    a=[]
    for i in range(2):
        num=input('num%s'%(i+1))
        a.append(num)
    print "Requesting %s+%s"%(a[0], a[1])
    print " %s"%(add_two_ints_client(a[0], a[1]))

   

