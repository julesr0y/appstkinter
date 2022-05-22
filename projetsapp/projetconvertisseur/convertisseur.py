#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 22:06:30 2022

@author: drroythomas
"""

def eurotodollar(montant):
    somme = montant * 1.1
    print(montant,"€ valent", somme,"$")
    
def dollartoeuro(montant):
    somme = montant * 0.9
    print(montant,"$ valent", somme,"€")
    
def eurotosterling(montant):
    somme = montant * 0.85
    print(montant,"€ valent", somme,"£")

def sterlingtoeuro(montant):
    somme = montant * 1.18
    print(montant,"£ valent", somme,"€")
    
def eurotoswitzerland(montant):
    somme = montant * 1.03
    print(montant,"€ valent", somme,"CHF")

def switzerlandtoeuro(montant):
    somme = montant * 0.97
    print(montant,"CHF valent", somme,"€")