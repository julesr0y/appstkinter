#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:05:31 2022

@author: drroythomas
"""

def palindrome(mot):
    motinverse = ''.join(reversed(mot))
    if mot == motinverse:
        print("Vrai")
    else:
        print("Faux")