import pandas as pd 
import matplotlib.pyplot as plt


data = pd.read_csv('data.csv')

print(data)
data['time'] = pd.to_timedelta(data['time'], unit='s').dt.total_seconds()
Vam = pd.Series([])

for index, row in data.iterrows():
    row['VAM'] = row['distance']*row['gradient']*10
    row['VAM'] = row['VAM']/row['time']*3600
    Vam = Vam.append(pd.Series([row['VAM']]), ignore_index = True)

data = data.assign(VAM = Vam)
print(data)
data.to_csv('data with vams.csv', sep=',', encoding='utf-8',index=False)


data_from_year = data[data['year'] > 2019]
groups = data_from_year.groupby('year')

for name, group in groups:
    plt.plot(group.gradient, group.VAM, marker='o', linestyle='',label=name)



plt.ylabel("VAM")
plt.xlabel("gradient of the climb")

plt.legend()
plt.show()
#data.plot(kind='scatter',x='gradient',y='VAM', s,color='red')
#plt.scatter(data.gradient, data.VAM, s=100, c=data.year, cmap='gray')
#plt.show()

#################################################
# plot the mean VAMS
plt.title("VAMs of the different climbs each year")
ddd = data.groupby('year', as_index=False).mean()
ddd = ddd.drop(['distance', 'gradient', 'time'], axis=1)
print(ddd)

#Stats = pd.read_csv('Statistics.csv')
#joined = pd.merge(ddd, Stats, how='inner', left_on = 'year', right_on = 'year')
#joined.to_csv('Statistics.csv', sep=',', encoding='utf-8', index=False)

plt.title("mean average VAM per year")
plt.plot(ddd.year, ddd.VAM, marker='o',label=name)
plt.xticks(ddd.year)
plt.ylabel("VAM")
plt.xlabel("year")
plt.show()
################################################

