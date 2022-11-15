#testing
import numpy as np
import matplotlib.pyplot as plt
r=np.array(list(range(0,541)))
l=[]
l1=[]
x = np.genfromtxt("PCOS_dataset.csv",skip_header=1, delimiter=",")
p1=np.empty(541)
r1=[]
r2=[]
# print(x)
for i in range(0,x.shape[0]):
    # print(x[i,2],"\t\t\t\t",i)
        if x[i,2]==0:
            l.append(x[i,6]) 
            r1.append(i)           
        elif x[i,2]==1:       
            l1.append(x[i,6])
            r2.append(i)
        

# p1=np.array(l)
# plt.subplot(311)
plt.plot(r1,l,'o')
plt.plot(r2,l1,'x')

#THIS IS CODE FOR MULTIPLE PLOTS 
#PLAYING WITH THIS IN THE WRONG WAY MIGHT CRASH SYSTEM
#PLEASE READ UP ON THIS BEFORE RUNNING
# for i in range(0,x.shape[0]):
#     # print(x[i,2],"\t\t\t\t",i)
#         if x[i,2]==0:
#             l.append(x[i,10]) 
#             r1.append(i)           
#         elif x[i,2]==1:       
#             l1.append(x[i,10])
#             r2.append(i)
# plt.subplot(312)
# plt.plot(r1,l,'o')
# plt.plot(r2,l1,'x')

# for i in range(0,x.shape[0]):
#     # print(x[i,2],"\t\t\t\t",i)
#         if x[i,2]==0:
#             l.append(x[i,14]) 
#             r1.append(i)           
#         elif x[i,2]==1:       
#             l1.append(x[i,14])
#             r2.append(i)
# plt.subplot(313)
# plt.plot(r1,l,'o')
# plt.plot(r2,l1,'x')
# plt.show()       




