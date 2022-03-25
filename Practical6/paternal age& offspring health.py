# To create a dictionary, key and values need to correspond one to one
# Make a scatter diagramm of the data
# For a given paternal age from	the input list above, print the	risk of	congenital heart disease for the offspring
paternal_age = [30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
chd = [1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94]
ages = {"30": 1.03, "35": 1.07, "40": 1.11, "45": 1.17, "50": 1.23, "55": 1.32, "60": 1.42, "65": 1.55, "70": 1.72,
        "75": 1.94}
print(ages)
import numpy as np
import matplotlib.pyplot as plt

x=(30, 35, 40, 45, 50, 55, 60, 65, 70, 75)
y=(1.03, 1.07, 1.11, 1.17, 1.23, 1.32, 1.42, 1.55, 1.72, 1.94)
plt.scatter(x,y,marker='*')
plt.xlabel("paternal age")
plt.ylabel("chd")
plt.show()
#variable(a) of this requested paternal age can be modified
a="30"
print("The risk of congenital heart disease in th offspring is "+str(ages[a]))
