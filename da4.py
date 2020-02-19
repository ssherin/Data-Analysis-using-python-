import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np 

data= pd.read_csv("Python_TestFiles_Sudoku_attemps.csv")
batch =data['Batch ID'].tolist()
gid = data['Game ID'].tolist()
tries = data['Tried'].tolist()
complete = data['Completed'].tolist()
x= np.arange(len(gid))
plt.bar(x,tries,width=0.60,label='Tried',color ='y')
plt.bar(x+0.60,complete,width=0.60,label='Completed',color= 'g')

plt.title("Sudoku Test Analysis")
plt.xlabel("Batch Range")
plt.ylabel("Attempts")
plt.legend(loc="upper right",shadow=True)
plt.grid()
plt.show()