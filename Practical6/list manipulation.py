#Rank Rob's eight points from lowest to highest
#Draw a boxplot from the data
#Calculate the average to see if Rob pass the exam
marks=[45,36,86,57,53,92,65,45]
marks.sort()
print(marks)
import numpy as np
import matplotlib.pyplot as plt
n=8
mark=(45,36,86,57,53,92,65,45)
plt.boxplot(mark,
            vert=True,
            whis=1.5,
            patch_artist=True,
            meanline=False,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False
                 )
plt.show()
print(np.mean(mark))
#Rob's average eight times was below 60.He failed.
