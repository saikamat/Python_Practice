#!/usr/bin/env python3

# this is a random class which gives positions of an object in space. 
# the position is given by vectors: x, y & z and is 0 at default.
class Twist(object):
    '''Creates a Maya vector/triple, having x, y and z coordinates as float values'''
    def __init__(self, x=0, y=0, z=0):
        self.x, self.y, self.z = x, y, z # values converted to float via properties


# this function returns which of the three axes was changed
def which_axis(Twist_obj, axis):
    setattr(Twist_obj, axis, 10)
    # change whichever code you want where axis is the keyword.


if __name__=='__main__':
    v=Twist(0,0,0)
    print("default position:")
    print(v.x, v.y, v.z)


    # command is take off
    which_axis(v, 'x')
    which_axis(v, 'y')
    print("after taking off:")
    print(v.x, v.y, v.z)


    # command is links
    which_axis(v, 'z')
    # which_axis(v, 'y')
    print("after taking left")
    print(v.x, v.y, v.z)
