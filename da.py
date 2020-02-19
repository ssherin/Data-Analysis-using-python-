import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

data= pd.read_csv("Python_Test_conditions.csv")
batch =data['Batch ID'].tolist()
solnA = data['Soln A Concentration'].tolist()
solnB = data['Soln B Concentration'].tolist()
solnC = data['Soln C Concentration'].tolist()
solnD = data['Soln D Concentration'].tolist()

#x= np.arange(len(batch))
plt.grid()
plt.plot(batch,solnA,label='Soln A',linewidth=0.5, marker='o',markersize=2)
plt.plot(batch,solnB,label='Soln B',linewidth=0.5, marker='*',markersize=2)
plt.plot(batch,solnC,label='Soln C',linewidth=0.5, marker='s',markersize=2)
plt.plot(batch,solnD,label='Soln D',linewidth=0.5, marker='h',markersize=2)
#plt.xticks(batch,data,fontsize=5,rotation=90)


plt.title("Concentration rates")
plt.xlabel("Batches")
plt.ylabel("Concentration")
plt.legend(loc="upper right",shadow=True)

plt.show()