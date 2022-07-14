# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 01:15:41 2022

@author: ditij
"""

nterms = int(input("How many terms?"))
n1 ,n2 = 0 ,1
count = 0
if nterms <=0:
    print("Please enter a positive integer")
elif nterms ==1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1