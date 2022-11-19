#! /usr/bin/env python

import rospy
import sys
from nav_msgs.srv import GetMap, GetMapRequest

# Initialise a ROS node
rospy.init_node('map_service_client')

#Wait for the serive client /traj_by_name to be running
rospy.wait_for_service('/static_map')

#Create a connection to the service
traj_by_name_service = rospy.ServiceProxy('/static_map', GetMap)

traj_by_name_object =GetMapRequest()

result = traj_by_name_service(traj_by_name_object)

#Prints result given by the service called
print(result.map.header)