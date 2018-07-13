#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include <base_control/wheel_speed.h>

double w1;
double w2;
double w3;
void callback(const base_control::wheel_speed&msg)//进入callback，处理车轮速度并且开始发布odom和广播tf
{

//bianmaqi return the speed of the wheel

    w1 = msg.x;
    w2 = msg.y;
    w3 = msg.z;
}

int main(int argc, char** argv)
{

    ros::init(argc, argv, "odometry_publisher");
    ros::NodeHandle n;
    ros::Publisher odom_pub = n.advertise<nav_msgs::Odometry>("odom", 50);
    tf::TransformBroadcaster odom_broadcaster;
    ros::Subscriber sub=n.subscribe("wheel_speed_topic",1000,callback);

    double pi=3.1416;
    double fi=pi/6;
    double R=0.03;
    double l=0.115;


    double x = 0.0;
    double y = 0.0;
    double th = 0.0;

    double vx = 0.0;
    double vy = 0.0;
    double vth = 0.0;

    ros::Time current_time, last_time;
    current_time = ros::Time::now();
    last_time = ros::Time::now();

    ros::Rate r(1.0);
    while(n.ok())
    {

        ros::spinOnce();               // check for incoming messages
        current_time = ros::Time::now();
        vx = 2*pi*R*(-0.5*w1+0.5*w3)/cos(fi);
        vy=2*pi*R*(0.5*w1-w2+0.5*w3)/(1+sin(fi));
        vth=2*pi*R*(0.5*w1+w2*sin(fi)+0.5*w3)/(1+sin(fi))/l;
        //compute odometry in a typical way given the velocities of the robot
        double dt = (current_time - last_time).toSec();
        double delta_x = (vx * cos(th) - vy * sin(th)) * dt;
        double delta_y = (vx * sin(th) + vy * cos(th)) * dt;
        double delta_th = vth * dt;

        x += delta_x;
        y += delta_y;
        th += delta_th;



        //since all odometry is 6DOF we'll need a quaternion created from yaw
        geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(th);//转动角度
        //first, we'll publish the transform over tf
        geometry_msgs::TransformStamped odom_trans;
        odom_trans.header.stamp = current_time;
        odom_trans.header.frame_id = "odom";
        odom_trans.child_frame_id = "base_link";
        odom_trans.transform.translation.x = x;
        odom_trans.transform.translation.y = y;
        odom_trans.transform.translation.z = 0.0;
        odom_trans.transform.rotation = odom_quat;

        //send the transform
        odom_broadcaster.sendTransform(odom_trans);

        //next, we'll publish the odometry message over ROS
        nav_msgs::Odometry odom;//声明一个odom的对象
        odom.header.stamp = current_time;
        odom.header.frame_id = "odom";

        //set the position发布位姿
        odom.pose.pose.position.x = x;
        odom.pose.pose.position.y = y;
        odom.pose.pose.position.z = 0.0;
        odom.pose.pose.orientation = odom_quat;

        //set the velocity发布速度
        odom.child_frame_id = "base_link";
        odom.twist.twist.linear.x = vx;
        odom.twist.twist.linear.y = vy;
        odom.twist.twist.angular.z = vth;

        //publish the message发布
        odom_pub.publish(odom);
        last_time = current_time;

        r.sleep();

        }
 //return 0;
}


