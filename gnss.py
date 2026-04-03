import pandas as pd
import matplotlib.pyplot as plt

# CGGTTS faylının yolu
#file_path = r"C:\Users\AzMI TF\OneDrive\Desktop\gnss_files\GMAZ0161.127"

# Faylı oxu (fixed width format)
#df = pd.read_fwf(file_path)

# Excel faylı kimi saxla
output_path = r"C:\Users\AzMI TF\OneDrive\Desktop\cggtts_output.xlsx"
#df.to_excel(output_path, index=False)

data = pd.read_excel(output_path)
y = data["REFSYS"]
z = data["SAT"]
n = z.shape[0]
x = list(range(n))
newdata = []
newx = []
for i in range(0, n):
         if z[i] ==5:
              newdata.append(i) == z[i]
              newx.append(i) == i
         else:
              continue
#new_n  = newdata.shape[0]
#print(newdata)

plt.scatter(newx,newdata)
plt.show()