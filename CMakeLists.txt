cmake_minimum_required(VERSION 2.8.3)
project(base_control)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  message_runtime
  roscpp
  rospy
  tf
  nav_msgs
)
add_message_files(
  FILES
  addtion.msg
  carspeed.msg
  wheelspeed.msg
  rate.msg


)


add_service_files(
   FILES
   addtwoints.srv
   request.srv
#   Service2.srv
)

generate_messages(
   DEPENDENCIES
   std_msgs  # Or other packages containing msgs
)


catkin_package(

)


include_directories(
  ${catkin_INCLUDE_DIRS}
)


add_executable(pub_test node/cpp/publishertest.cpp)
target_link_libraries(pub_test ${catkin_LIBRARIES})
add_dependencies(pub_test base_control_generate_messages_cpp)

add_executable(subscribertest node/cpp/subscribertest.cpp)
target_link_libraries(subscribertest ${catkin_LIBRARIES})
add_dependencies(subscribertest base_control_generate_messages_cpp)



add_executable(odompublisher node/cpp/odompublisher.cpp)
target_link_libraries(odompublisher ${catkin_LIBRARIES})
add_dependencies(odompublisher base_control_generate_messages_cpp)



add_executable(base_link_to_camera_link node/cpp/base_link_to_camera_link.cpp)
target_link_libraries(base_link_to_camera_link  ${catkin_LIBRARIES})
add_dependencies(base_link_to_camera_link base_control_generate_messages_cpp)

add_executable(camera_link_to_laser node/cpp/camera_link_to_laser.cpp)
target_link_libraries(camera_link_to_laser  ${catkin_LIBRARIES})
add_dependencies(camera_link_to_laser base_control_generate_messages_cpp)

add_executable(data_publisher node/cpp/data_publisher.cpp)
target_link_libraries(data_publisher  ${catkin_LIBRARIES})
add_dependencies(data_publisher base_control_generate_messages_cpp)



