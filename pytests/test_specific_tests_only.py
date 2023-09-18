
## check if the polygon plot points are a square or not
## 
##             .(bx, by)               .(cx, cy)
##
##
##
##
##            .(ax, ay)                .(dx, dy)
##

import pytest

@pytest.mark.xfail
def test_SquarePolygons():
    ax = 0
    ay = 0
    bx = 0
    by = 100
    cx = 100
    cy = 100
    required_dx = 100
    required_dy = 0
    assert required_dx == 100, "X co-ordinate of D vertex is incorrect"
    assert required_dy == 10, "Y co-ordinate of D vertex is incorrect"

@pytest.mark.skip
def test_SignCheck():
    sign_read = "STOP"
    assert sign_read == "HALT", "Sign is not the Stop sign"

