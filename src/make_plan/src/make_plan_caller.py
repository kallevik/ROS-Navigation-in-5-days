#! /usr/bin/env python 

import rospy 
from nav_msgs.srv import GetPlan, GetPlanRequest

rospy.init_node('service_client')
rospy.wait_for_service('/move_base/make_plan')

#rosservice info /move_base/make_pan: type: nav_msgs/GetPlan
make_plan_service = rospy.ServiceProxy('/move_base/make_plan', GetPlan)

my_msg = GetPlanRequest()
my_msg.start.header.frame_id = 'map'
my_msg.start.pose.position.x = 0.0
my_msg.start.pose.position.y = 0.0
my_msg.start.pose.position.z = 0.0
my_msg.start.pose.orientation.x = 0.0
my_msg.start.pose.orientation.y = 0.0
my_msg.start.pose.orientation.z = 0.0
my_msg.start.pose.orientation.w = 0.0

my_msg.goal.header.frame_id = 'map'
my_msg.goal.pose.position.x = 1.0
my_msg.goal.pose.position.y = 2.0
my_msg.goal.pose.position.z = 0.0
my_msg.goal.pose.orientation.x = 0.0
my_msg.goal.pose.orientation.y = 0.0
my_msg.goal.pose.orientation.z = 0.0
my_msg.goal.pose.orientation.w = 0.0

result = make_plan_service(my_msg)
print(result)

