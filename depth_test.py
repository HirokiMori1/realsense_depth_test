#! /usr/bin/env python
# -*- coding: utf-8 -*- 
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image, CameraInfo
from cv_bridge import CvBridge, CvBridgeError


class Depth:
    def __init__(self):

        self.depth_sub = rospy.Subscriber('/camera/depth/image_rect_raw', Image, self.callback)
        self.bridge = CvBridge()


    def callback(self, data):
        #Image型をOpenCVの画像に変換
        depth = self.bridge.imgmsg_to_cv2(data, 'passthrough')
        #画像中心の距離を出力
        print(depth[240,320])


if __name__ == "__main__":
    rospy.init_node("depth_test")
    depth = Depth()
    rospy.spin()