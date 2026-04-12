import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CGGTTS faylının yolu
#file_path = r"C:\Users\AzMI TF\OneDrive\Desktop\gnss_files\GMAZ0161.129"

#Faylı oxu (fixed width format)
#df = pd.read_fwf(file_path)

# Excel faylı kimi saxla
output_path = r"C:\Users\AzMI TF\OneDrive\Desktop\cggtts_output_1.xlsx"
#df.to_excel(output_path, index=False)


df = pd.read_excel(output_path)
y = df["REFSYS"]
z = df["SAT"]
ch = df["FRC"]
n = len(z)

newdata = []  # z[i] ==27 or z[i] ==5 or
newx = []
for i in range(0, n):
         
         if  ch[i]=="L3C" or ch[i]=="L3C":
              newdata.append(0.1*y[i])  
              newx.append(i)
       
         elif i==6000:
              break
              
#new_n  = newdata.shape[0]
#print(newdata)

plt.scatter(newx,newdata)
plt.show()
#print(newx,newdata)
coeff = np.polyfit(newx,newdata,1)
m, b = coeff
#y_fit = m*int(newx) + b
plt.legend()
#plt.plot(newx,y_fit, color = "red")
