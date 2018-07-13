#!/usr/bin/env python
import sys
import rospy
from smartcar.srv import request

def local_client(x):
    rospy.wait_for_service('bridge_service')
    try:
        client = rospy.ServiceProxy('bridge_service', request)
        resp1 = client(x)
        return resp1
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

def usage():
    return "%s [x y]"%sys.argv[0]
if __name__ == "__main__":
    x = str(sys.argv[1])
    print "request the service: %s"%(x)
    print " %s"%(local_client(x))