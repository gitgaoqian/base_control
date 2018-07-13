# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 08:52:21 2017

@author: ros
"""
import requests
import os
import thread


#some functions about cloud service 
#查询云端服务
def cloud_service_find(url):
    r=requests.get(url)
    return r.text
   
#检测网络的质量    
def net_check(ipaddress):
    count=os.popen('ping -c 20 -i 0.2'+' '+ipaddress+' '+' | grep "received" | cut -d "," -f 2| cut -d " " -f 2')
    num=count.read()
    packet_loss=(20-int(num))*100/20
    return packet_loss
#云端环境变量的设置    
def cloud_param_set(url,master_uri):
    value={'ros_master_uri':master_uri}
    r = requests.post( url, data=value)
    return r.text

#根据不同表示服务的ｕrl实现不同云端服务的请求    
def cloud_service_request(url):
    r = requests.post( url)
    print r.text

def cloud_service_stop(url):
    r=requests.post(url)
    print r.text
    
#some functions about local service 
def two_ints_addition_launch():
    os.system('rosrun smartcar addtwointserver.py')
def gmapping_launch():
    os.system('rosparam set use_sim_time true ')
    os.system('rosrun gmapping slam_gmapping scan:=base_scan')
def local_node_launch(service):
    if service=='two_ints_addition':
        thread.start_new_thread(two_ints_addition_launch,())
    elif service=='gmapping':
        thread.start_new_thread(gmapping_launch,())
    else:
        print "no service in the local"
        
def service_stop(service):
     if service=='two_ints_addition':
         os.system('rosnode kill add_two_ints_server')
     elif service=='gmapping':
         os.system('rosnode kill slam_gmapping')
     else:
         print "the serive you want to stop doesn't exist"
     print "stop service"
   


  
