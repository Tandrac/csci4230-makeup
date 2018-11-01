# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 14:16:28 2018

@author: Tommy
"""
import random

def factor(num):
    counter = 0
    while(num%2 == 0):
        counter+=1
        num = num/2
    return (counter, num)


def millerRabin(n, k):
    factors = factor(n-1)
    r = int(factors[0])
    d = int(factors[1])
    for i in range(k):
        a = random.randint(2,n-2)   
        #print(d)
        #test = pow(a,d,n)
        x = (a**d)%n

        if x == 1 or x == n-1:
            return True
            
        else:
            for j in range(r-1):
                x = (x**2)%n
                if x == n-1:
                    return True
    return False

def main():
    n = [31531, 520482, 485827, 15485863]
    k = 5
    for i in n:
        temp = millerRabin(i, k)
        print(i,": ",temp)
    print("Done")

if __name__ == "__main__":
    main()