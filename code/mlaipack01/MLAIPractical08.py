#!/usr/bin/env /home/haozeke/.venvs/ictAI/bin/python

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    n=np.size(x)
    m_x=np.mean(x)
    m_y=np.mean(y)
    SS_xy=np.sum(x*y-n*m_x*m_y)
    SS_xx=np.sum(x*x-n*m_x*m_x)
    m=SS_xy/SS_xx
    c=m_y-m*m_x
    return [m,c]
def plot_regression_line(x,y,b):
    plt.scatter(x,y, color="m",
                marker="o",s=30)
    y_pred=b[1]*x+b[0]
    plt.scatter(x,y_pred,color="g")
    plt.plot(x,y_pred,color="b")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

def main():
    x = np.array([0,1,2,3,4,5,6,7,8,9])
    y = np.array([1,3,2,5,7,8,8,9,10,12])
    m,c=estimate_coef(x,y)
    print("Estimated coefficients:\n")
    print("slope m = ",m)
    print("y-intercept c = ",c)
    plot_regression_line(x,y,[c,m])

if __name__ =="__main__":
    main()
