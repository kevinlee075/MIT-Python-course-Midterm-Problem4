# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 16:21:34 2021

@author: Lenovo
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    for i in range(len(L)):
        L[i].reverse()