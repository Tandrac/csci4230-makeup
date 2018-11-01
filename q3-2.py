# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 20:49:49 2018

@author: Tommy
"""

def g(x,n):
    return(x**2+1)%n

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def polRho(n):
    
    d = 1
    x=2
    y=2
    
    while (d == 1):
        x = g(x,n)
        y = g(g(y,n),n)
        d = gcd(abs(x-y), n)
        
    if d == n:
        return False
    else:
        return d

def main():
    n = [31531, 520482, 485827, 15485863]
    for i in n:
        print(polRho(i))



if __name__ == "__main__":
    main()