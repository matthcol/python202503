"""unit tests on class Point"""

# Test à exécuter avec le framework pytest
# conda install pytest
#   ou
# pip install pytest

from geometry import Point

def test_distance():
    ptA = Point(x=1.5, y=2.25, name='A')
    ptB = Point(x=4.5, y=6.25, name='B')
    d = ptA.distance(ptB)
    assert 5.0 == d

def test_fail():
    assert True == False
