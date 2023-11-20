# -*- coding: utf-8 -*-
"""
Name: Ian Collins
KUID: 3051520
Course: MATH 320
Date: 11/19/23
Purpose: Simulate Euler's Formula and do a linear approximation of a curve
"""

import pandas as pd
import matplotlib.pyplot as plt
import cmath as c

def dydx(y):
    return 5-3*c.sqrt(y)

def fy(t):
    con = c.sqrt(2)+5/3
    return (con*(c.e**t)-(5/3))**2

def create_dataset(i):
    #set vars
    y = 2
    t = 0
    h = [.01, .1, 1]
    
    #open and write to file
    with open(f'data{i}.txt', 'w') as data:
        data.write('Y,T\n')
        data.write(f'{y},{t:2f}\n')
        while t < 3:
            t += h[i]
            y = fy(t) + dydx(y)*h[i]
            data.write(f'{y.real},{t:.2f}\n')
            

def print_plot():
    #open data set
    frame0 = pd.read_csv('data0.txt')
    t0 = frame0['T']
    y0 = frame0['Y']
    frame1 = pd.read_csv('data1.txt')
    t1 = frame1['T']
    y1 = frame1['Y']
    frame2 = pd.read_csv('data2.txt')
    t2 = frame2['T']
    y2 = frame2['Y']
    
    #create plot
    plt.plot(t0,y0, 'g',label='h=0.01')
    plt.plot(t1,y1,'b',label='h=0.1')
    plt.plot(t2,y2,'r',label='h=1')
    plt.legend()
    plt.title("Linear Approximation using Euler's method for \ny(t)=((sqrt(2)+5/3)e^t-5/3)^2")
    plt.xlabel('Time (t)')
    plt.ylabel('y(t)')
    plt.yticks([0,500,1000,1500,2000,2500,3000,3500,4000])
    
    #show plot
    plt.show()
    
def main():
    for i in range(3):
        create_dataset(i)
    
    print_plot()
    
if __name__=='__main__':
    main()