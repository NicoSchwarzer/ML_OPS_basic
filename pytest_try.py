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
  if x <= max_num:
    return x + 5
  else:
    raise Exception("lower number!")



class fruit:
  def __init__(self, name):
    self.name = name

  
## another  class

class fruit_2(): # inherits from fruit 

  def __init__(self, name: str,  size: float, weight: float):

    super().__init__()

    self.size = size
    self.weight = weight 
    self.name  = name

  def weight_per_size(self):
    return self.weight / self.size 




