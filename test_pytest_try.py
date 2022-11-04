

from pytest_try import fruit_2, func
from pytest_try import fruit, fruit_2
import numpy as np 
import pytest



def test_func():  # important to have test in the beginning!
    #pass
    assert func(3, 10) ==  8


def test_two():  ## running only this test via 'test_pytest_try.py::test_two' in the console!
    #x = np.random.rand(10)
    assert func(3,2) ==  8



## now only running "pytest" in the console works! 


def test_fruit():
    fruit1 = fruit("apple")
    assert fruit1.name == "apple"


## fixtures 

@pytest.fixture
def apple():
    return fruit("apple")

# test with fixture 
def test_fruit_fix(apple):
    assert apple.name == "apple"


## more comploex fixture 

@pytest.fixture
def complex_apple():
    return fruit_2("apple2", 20, 20)

def test_complex_fruit(complex_apple):
    assert complex_apple.weight_per_size() == 1 


