#!/usr/bin/env python
import rospy
from smartcar.srv import request
import ros_client as bridge_client
import time
def handle_request(data):
    if data.req=='list':
        url="http://219.216.116.102:5566/cloud_service/list"
        return bridge_client.cloud_service_find(url) 
    elif data.req=='stop':
        url="http://219.216.116.102:5566/cloud_service/stop"
        bridge_client.cloud_service_stop(url)
        return 'cloud_node killed'
        
    packet_loss=bridge_client.net_check('219.216.116.102')
    if packet_loss<5:
        flag=0
    else:
        flag=1
    service=data.req  
    while 1:
        packet_loss=bridge_client.net_check('219.216.116.102')
        if packet_loss<5 and flag==0:
            bridge_client.cloud_param_set('http://219.216.116.102:5566/cloud_service/setparam','http://219.216.116.99:11311')
            bridge_client.service_stop(service)
            time.sleep(1)
            url="http://219.216.116.102:5566/cloud_service/"+service
            bridge_client.cloud_service_request(url)
            flag=1
        elif packet_loss<5 and flag==1:
            print "net is good"
        elif packet_loss>=5 and flag==1:
            bridge_client.local_node_launch(service)
            flag=0
        elif packet_loss>=5 and flag==0:
            print "net is bad"
        else:
            print "error!"
    return "the request is interrupted"
#def handle_list(data):

def bridge_server():
    rospy.init_node('bridge_server')
    rospy.Service('bridge_service', request, handle_request)
   # rospy.Service('service_find', request,handle_list)
    print "bridge_server ready for client."
    rospy.spin()
if __name__ == "__main__":
     bridge_server()





