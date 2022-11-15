import csv
import matplotlib as mp
import numpy as np

def toflt(a,cnt):
    a1=[]
    for i in a:
        
        try:
            if (type(eval(i)))=='<class \'int\'>':
                print("int")
                a1.append(int(i))
            elif (type(eval(i)))=="<class \'float\'>":
                print("float")
                a1.append(float((i)))
        except Exception as e:
            pass
    #print(a1,"\t\t\t\t\t",cnt)#debug_2
    return a1
        

f=open("PCOS_dataset.csv","r")
readerobj=csv.reader(f)
c=0
x=np.empty((541,44),float)
for row in readerobj:
    if c==0:
        c+=1
        continue
    else:
        r1=toflt(row,c)
        print(np.array(r1))#debug_1
        #np.append(x,np.array(r1))
    c+=1
# print(x)
# for i in range(0,len(x)-1):
#     print(x[i,2])

#csv to numpy


    
