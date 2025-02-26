#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side

assert hypotenuse(3,4,True) == 5
(2 points)
"""
import math

def hypotenuse(a,b, side):
    a=int(a)
    b=int(b)
    if a==True or b==True:
        side=math.sqrt(a**2+b**2)
        print(f"{side}")
        return side
    elif side==False:
        side=math.sqrt(max(a,b)**2-min(a,b)**2)
        print(f"{side}")
    return False



if __name__ == "__main__":
    assert hypotenuse(3,4,True) == 5
    assert hypotenuse(5,12,True) == 13
    assert hypotenuse(3,5,False) == 4
    assert hypotenuse(13,12,False) == 5