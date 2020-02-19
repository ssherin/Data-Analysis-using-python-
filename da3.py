import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

data= pd.read_csv("Python_Test_conditions.csv")
batch =data['Batch ID'].tolist()
humidity = data['Relative Humidity'].tolist()
noise = data['White Noise (db)'].tolist()

#x= np.arange(len(batch))
plt.grid()
plt.plot(batch,humidity,label='Relative Humidity',color ='r',linewidth=0.5, marker='o',markersize=2)
plt.plot(batch,noise,label='White Noise',color= 'm',linewidth=0.5, marker='*',markersize=2)


plt.title("Concentration rates")
plt.xlabel("Batches")
plt.ylabel("Conditions")
plt.legend(loc="upper right",shadow=True)

plt.show()