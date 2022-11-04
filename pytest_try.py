# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 11:50:27 2022

@author: Nico
"""

### PyTest ### 

import pandas as pd 
import numpy as np
import pytest


def func(x: float, max_num: int) -> float:
  '''
  This function adds 5 to the first input (float) if it does not exceed the second input (float )
  '''
  if x <= max_num:
    return x + 5
  else:
    raise Exception("lower number!")



class fruit:
  '''
  Easy class with just one attribute 
  '''
  def __init__(self, name):
    self.name = name

  
## another  class

class fruit_2(fruit): # inherits from fruit 
  '''
  Another classed based on the fruit class (inherits from it). 
  It has more input arguments (sie and weight - both float) and one function based on the latter
  '''
  def __init__(self, name: str,  size: float, weight: float):

    super().__init__()

    self.size = size
    self.weight = weight 
    self.name  = name

  def weight_per_size(self):
    return self.weight / self.size 




