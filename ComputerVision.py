from Math import *
from Physics import *
from Others import *
import cv2
import os
import numpy as np
from matplotlib import pyplot as plt

def MatchImageTemplateInOpencv2 (
        HayStackImg = '',
        NeddleImg = '', 
        ImgReadMethod = cv2.IMREAD_UNCHANGED,
        MatchTemplateMethod = cv2.TM_CCOEFF_NORMED,
        ConfidenceThreshold = 0.7,
        RectangleColour = (0, 255, 0),
        RectanlgeLineType = cv2.LINE_4,
        RectangleThickness = 2,

        FrameName = 'frame',

        FoundMsg = None,
        NotFoundMsg = None
) :
    
    haystack_img = cv2.imread(HayStackImg, ImgReadMethod)
    needle_img = cv2.imread(NeddleImg, ImgReadMethod)

    result = cv2.matchTemplate(haystack_img, needle_img, MatchTemplateMethod)

    threshold = ConfidenceThreshold

    locations = np.where(result >= threshold)

    locations = list(zip(*locations[::-1]))

    if locations :
        print(FoundMsg)

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]

        line_colour = RectangleColour
        line_type = RectanlgeLineType

        for loc in locations :
            top_left = loc
            bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)

            cv2.rectangle(haystack_img, top_left, bottom_right, line_colour, thickness = RectangleThickness)

        cv2.imshow(FrameName, haystack_img)

        cv2.waitKey()

    else :
        print(NotFoundMsg)