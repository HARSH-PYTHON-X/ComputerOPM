from time import sleep
from tkinter import *
import random
import math

#* random stuff

def random_int (start = 1, end = 9) :
    ran = random.randint(start, end)
    
    return ran

def choose_random (choose_from, length = 1) :
    ran = ''.join(random.sample(choose_from, length))
    return ran

def RandomChoiceSelector (_choices_, _no_of_output_ = 1) :
    outcome = ''.join(random.sample(_choices_, _no_of_output_))
    
    return outcome

#* Real Numbers

class RealNumber :
    def LCMof2Nums (x, y) :
        if x > y:
            greater = x
        else:
            greater = y

        while(True):
            if((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1

        return lcm

    def HCFof2Nums (x, y) :
        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller+1):
            if((x % i == 0) and (y % i == 0)):
                hcf = i 
        return hcf 


#* COORDINATE GEOMETERY

class CordGeo :
    def GetCordsOfObjectByMiddleSection (pointA = (0, 0), middlePoint = (0, 0)) :
        pointBx = (middlePoint[0] * 2) - pointA[0]
        pointBy = (middlePoint[1] * 2) - pointA[1]

        return (pointBx, pointBy)

    def GetDistanceBetweenTwoObjectsByDistanceFormula (pointA = (0, 0), pointB=  (0, 0)) :
        withoutRootDistanceXofAB = (pointB[0] - pointA[0]) 
        withoutRootDistanceYofAB = (pointB[1] - pointA[1])

        squaredXofAB = withoutRootDistanceXofAB * withoutRootDistanceXofAB
        squaredYofAB = withoutRootDistanceYofAB * withoutRootDistanceYofAB

        distance = math.sqrt(squaredXofAB + squaredYofAB)

        return distance
    
#* TRIGNOMETERY

class Trigno :
    pass

#* Arithemetic Progression

class AP :
    def n_term_of_AP (AP, term_no) :
        global d, a, n, n_th_term
        d = 0

        if len(AP) >= 4 :
            if AP[1] - AP[0] == AP[3] - AP[2] :
                d = AP[1] - AP[0]

        elif len(AP) <= 3 :
            d = AP[1] - AP[0]

        a = AP[0]

        n = term_no

        n_th_term = a + (n - 1) * d

        return n_th_term

    def no_of_term_in_AP (AP, term_digit) :
        global d, a, num, an

        d = 0

        if len(AP) >= 4 :
            if AP[1] - AP[0] == AP[3] - AP[2] :
                d = AP[1] - AP[0]

        elif len(AP) <= 3 :
            d = AP[1] - AP[0]

        a = AP[0]

        num = term_digit

        n = ((num - a) / d) + 1

        return n


#* Surface Area and Volume

class SAV :
    def convertInLitres (volume) :
        return volume * 1000


    def CuboidTSA (l, b, h) :
        TSA = 2 * (l * b + b * h + h * l)
        return TSA

    def CuboidLSA (l, b, h) :
        LSA = 2 * h (l + b)
        return LSA

    def CuboidVOLUME (l, b, h) :
        VOLUME = l * b * h
        return VOLUME

    # CUBE

    def CubeTSA (side) :
        TSA = 6 * side * side
        return TSA

    def CubeLSA (side) :
        LSA = 4 * side * side
        return LSA

    def CubeVOLUME (side) :
        VOLUME = side * side * side
        return VOLUME

    # CYLINDER

    def CylinderTSA (r, h) :
        TSA = 2 * 3.14 * r * (r + h)
        return TSA

    def CylinderLSA (r, h) :
        LSA = 2 * 3.14 * r * h
        return LSA

    def CylinderVOLUME (r, h) :
        VOLUME = 3.14 * r * r * h
        return VOLUME

    # SPHERE

    def SphereTSA (r) :
        TSA = 4 * 3.14 * r * r
        return TSA

    def SphereVOLUME (r) :
        VOLUME = 4 / 3 * 3.14 * r * r * r
        return VOLUME

    # HEMISPHERE

    def HemisphereTSA (r) :
        TSA = 3 * 3.14 * r * r
        return TSA

    def HemisphereLSA (r) :
        LSA = 2 * 3.14 * r * r
        return LSA

    def HemisphereVOLUME (r) :
        VOLUME = 2 / 3 * 3.14 * r * r * r
        return VOLUME

    # CONE

    def CONEfindL (r, h) :
        l = (r * r + h * h) ** 0.5
        return l

    def CONEfindR (l, h) :
        r = (h * h - l * l) ** 0.5
        return r

    def CONEfindH (l, r) :
        h = (l * l - r * r) ** 0.5
        return h

    def ConeTSA (r, l) :
        TSA = 3.14 * r * (r + l)  
        return TSA

    def ConeLSA (r, l) :
        TSA = 3.14 * r * l

    def ConeVOLUME (r, h) :
        VOLUME = 1 / 3 * 3.14 * r * r * h
        return VOLUME