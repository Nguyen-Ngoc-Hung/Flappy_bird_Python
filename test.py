from random import randint
import pygame
import random
arr = []
for i in range(1,11):
    temp=[i,i+1]
    arr.append(temp)
del arr[1][1]
print(arr)
print(arr[1])