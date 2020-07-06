import codecademylib3_seaborn
import pandas as pd
import numpy as np
from scipy import stats
from weather_data import london_data
print(london_data.head())
print(london_data.iloc[100:200])
print(len(london_data))
temp=london_data["TemperatureC"]
average_temp=np.average(temp)
print("avg_temp",average_temp)
temperature_var=np.var(temp)
print("var_temp",temperature_var)
temperature_standard_deviation=np.std(temp)
print("std_temp",temperature_standard_deviation)

print(london_data.head())
june=london_data.loc[london_data["month"]==6]["TemperatureC"]
july=london_data.loc[london_data["month"]==7]["TemperatureC"]
mean_temp_june=np.mean(june)
print(mean_temp_june)
mean_temp_july=np.mean(july)
print(mean_temp_july)
print("std_june",np.std(june))
print("std_july",np.std(july))
for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")
