import pandas as pd 
import matplotlib.pyplot as plt


'''
Reads the Statistics file and plots various metrics for each year TDF
'''

data = pd.read_csv('Statistics.csv')

data = data[data['year']>2014]

figs,axs = plt.subplots(5)
y = [3200,3300,3400,3500,3600,3700]

axs[0].set_title("TDF distance by year")
axs[0].plot(data.year, data.distance, marker='o')
axs[0].set_yticks(y)
axs[0].set_xticks(data.year)


axs[1].set_title("TDF speed by year")
axs[1].plot(data.year, data.speed, marker='o')
axs[1].set_xticks(data.year)

y_elevationtot = [0,30000,60000]
axs[2].set_title("elevation gain by year")
axs[2].plot(data.year, data.elevationgain, marker='o')
axs[2].set_yticks(y_elevationtot)
axs[2].set_xticks(data.year)

y_elevation = [0,10,20]
axs[3].set_title("elevation gain per km")
axs[3].plot(data.year, data.elevationperkm, marker='o')
axs[3].set_yticks(y_elevation)
axs[3].set_xticks(data.year)

y_temperature = [0,10,20,30,40]
axs[4].set_title("temperature")
axs[4].plot(data.year, data.temperature, marker='o')
axs[4].set_yticks(y_temperature)
axs[4].set_xticks(data.year)

figs.tight_layout(pad=0.5)
plt.show()




'''
mean_dataframes = pd.DataFrame(columns = ['meanSpeed', 'meanDistance', 'meanTemperature','meanVAM'])

 
# append mean stats to meanStats

mean_dataframes = mean_dataframes.append({'meanSpeed' : data['speed'].mean(), 'meanDistance' : data['distance'].mean(), 'meanTemperature' : data['temperature'].mean(), 'meanVAM' : data['VAM'].mean()},
        ignore_index = True)
print(mean_dataframes)
mean_dataframes.to_csv('meanStats.csv', sep=',', encoding='utf-8', index=False)
'''