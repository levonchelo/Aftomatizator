#import pytest
from calculator import Calculator

cal = Calculator( )


#@pytest.mark.skip
def test_sum_positive_nums():
    cal = Calculator( )
    res = cal.sum(8,2)
    assert res == 10
def test_sum_negative_nums():
    cal = Calculator( )
    res = cal.sum(-6,-2)
    assert res == -8
def test_sum_positive_and_neqative_nums():
    cal = Calculator( )
    res = cal.sum(8,-2)
    assert res == 6


#print ('start')
#res = cal.sum(8,2)
#assert res == 10

#res = cal.sum(-6, -10)
#assert res == -16

#res = cal.sum (5.6 , 4.3)
#res = round (res,1)
#assert res == 9.9



#numbers = [1,2,3,4,5,6,7,8,9,5]
#res = cal.avg(numbers)
#assert res == 5
#print ('finish')

#res = cal.div (10,0)
#assert res == None