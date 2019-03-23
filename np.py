#-*- coding:utf-8 -*-
#Author: aeadod

import numpy as np
vec=np.array([1,2,3])
vec.shape
vec.size
vec.ndim
type(vec)

matrix=np.array([[1,2],[3,4]])

matrix.shape
matrix.ndim
matrix.size
type(matrix)

one=np.arange(12)
one
one.reshape((3,4))
two=one.reshape((3,4))
two.ndim
zeros=np.zeros((3,4))
ones=np.ones((5,6))
ident=np.eye(4)

