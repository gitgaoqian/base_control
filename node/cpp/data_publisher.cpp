#include <ros/ros.h>
#include <std_msgs/Float64.h>


int main(int argc, char **argv)
{

  ros::init(argc, argv, "data_publisher");
  ros::NodeHandle n;
  ros::Publisher Data_pub = n.advertise<std_msgs::Float64>("Data", 1000);
  ros::Rate loop_rate(10);
  float count = 0;
  while (ros::ok())
  {
    
    std_msgs::Float64 msg;
    msg.data = sin(count);
    Data_pub.publish(msg);
    
    ros::spinOnce();

    loop_rate.sleep();

    count = count + 0.1;
  }


  return 0;
}

