# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 16:05:08 2023

@author: b.wolpensinger
"""

a = 3
import numpy as np
np.array 




#%%
#import random
print('a')
print('b')
print('c')
#for i in range(10):
#    x = random.random() # random from 0.0 to 1.0 but not including
#    print(x)
#%%



# Grade exercise

def computegrade(score):
    try:
        score = float(score)
    except:
        print("No number entered")
    if score < 0 and score > 1:
        print("The score is out of range")
    if score >= 0.9:
        print("A")
    elif score >= 0.8:
        print("B")
    elif score >= 0.7:
        print("C")
    elif score >= 0.6:
        print("D")
    else:
        #if score < 0 
        print("F")
        
computegrade(0.7)