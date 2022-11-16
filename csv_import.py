import csv
import matplotlib.pyplot as mp
import numpy as np



f=open("PCOS_dataset.csv","r")
readerobj=csv.reader(f)
c=0
x = np.genfromtxt("PCOS_dataset.csv",skip_header=1, delimiter=",")

X=[]
Y=[]
Z=[]
for i in range(0,x.shape[0]):
    X.append(x[i,2])
    Y.append(x[i,6])
    Z.append(x[i,5])
mp.plot(X,Y,'o')
mp.plot(X,Z,'x')
mp.show()