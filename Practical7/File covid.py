import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/cygwin64/home/17847/IBI1_2021-22/IBI1_2021-22/Practical7")
os.getcwd()
covid_data=pd.read_csv("full_data.csv")
print(covid_data.iloc[8:19,0:3:2]) # This shows rows 10 through 20 in the table
#Verify Afghanistan from the first line
#Until you get to the last line
#Print them out
n=0
my_columns = [False, False, False, False, True, False]
my_row=[]
while n<=7995:
    if covid_data.iloc[n,1]=="Afghanistan":
      my_row.append(True)
      n+=1
    else:
      my_row.append(False)
      n+=1
print(covid_data.loc[my_row,my_columns])
covid_china_data=pd.read_csv("china_new_data.csv")
new_cases=covid_china_data.iloc[0:91,2]
new_deaths=covid_china_data.iloc[0:91,3]
print(np.mean(new_cases))
print(np.mean(new_deaths))
plt.title('boxplot of new cases and new deaths',fontsize=15)
label='new cases','new deaths'
plt.boxplot([new_cases,new_deaths],
            vert=True,
            patch_artist=True,
            meanline=True,
            showmeans=True,
            showbox=True,
            showcaps=True,
            showfliers=True,
            notch=False,
            labels=label)
plt.show() # I didn't delete the outliers, and some of the outliers are so big that the whole picture doesn't look very harmonious
china_dates=covid_china_data.iloc[0:91,0]
plt.figure(figsize=(13,6))
plt.title('changes in new cases and deaths over time in China',fontsize=15)
plt.plot(china_dates, new_cases, '+',color='green')
plt.plot(china_dates, new_deaths, '+',color='blue')
plt.text(0,15000,'green represents new cases',fontdict=None)
plt.text(0,14000,'blue represents new deaths',fontdict=None)
plt.xticks(china_dates.iloc[0:len(china_dates):4],rotation=-20)
plt.xlabel("dates")
plt.ylabel("new cases and deaths")
plt.show()
covid_USA_data=pd.read_csv("USA_data.csv")
latest_total_deaths=covid_USA_data.iloc[91,5]
latest_total_cases=covid_USA_data.iloc[91,4]
proportion='{:.2%}'.format(latest_total_deaths/latest_total_cases)
print('The proportion of cases has died in the USA is'+str(proportion))
USA_new_cases=covid_USA_data.iloc[0:91,2]
USA_total_cases=covid_USA_data.iloc[0:91,4]
USA_dates=covid_USA_data.iloc[0:91,0]
plt.figure(figsize=(13,6))
plt.title('new cases and total cases developed over time in the USA',fontsize=15)
plt.plot(USA_dates, USA_new_cases, '+',color='green')
plt.plot(USA_dates, USA_total_cases, '+',color='blue')
plt.text(0,140000,'green represents new cases',fontdict=None)
plt.text(0,130000,'blue represents total cases',fontdict=None)
plt.xticks(USA_dates.iloc[0:len(USA_dates):4],rotation=-20)
plt.xlabel("dates")
plt.ylabel("new cases and total cases")
plt.show()