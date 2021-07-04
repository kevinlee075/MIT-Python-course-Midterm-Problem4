# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 16:21:34 2021

@author: Lenovo
"""

#Implement a function that meets the specifications below.
#For example, if L = [[1, 2], [3, 4], [5, 6, 7]] then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    L.reverse()
    for i in range(len(L)):
        L[i].reverse()