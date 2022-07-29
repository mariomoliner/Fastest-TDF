import pandas as pd 
import matplotlib.pyplot as plt

Stats = pd.read_csv('Statistics.csv')
meanStats = pd.read_csv('meanStats.csv')

difficulty_dataframe = pd.DataFrame(columns = ['year', 'type1', 'type2', 'type3'])

def calc_difficulty(nSpeed, nVAM, nDistance, nTemperature, type):
    diff = 0;
    if(type==1):
        diff = 0.45*nVAM + 0.02*nDistance + 0.45*nSpeed + 0.08*nTemperature;
    if(type==2):
        diff = 0.6*nVAM + 0.02*nDistance + 0.3*nSpeed + 0.08*nTemperature;
    if(type==3):
        diff = 0.3*nVAM + 0.02*nDistance + 0.6*nSpeed + 0.08*nTemperature;
    return diff

Stats = Stats[Stats['year'] > 2015]
print(Stats)
for index, row in Stats.iterrows():
    print(row['year'])
    nTemp = row['temperature']/meanStats.at[0,'meanTemperature']
    nSpeed = row['speed']/meanStats.at[0,'meanSpeed']
    nDist = row['distance']/meanStats.at[0,'meanDistance']
    nVAM = row['VAM']/meanStats.at[0,'meanVAM']
    diff = []
    for i in range(3):
        diff.append(calc_difficulty(nSpeed, nVAM, nDist, nTemp, i+1))
    
    difficulty_dataframe = difficulty_dataframe.append({'year' : row['year'], 'type1' : diff[0], 'type2' : diff[1], 'type3' : diff[2]},
        ignore_index = True)

figs,axs = plt.subplots(3)

print(difficulty_dataframe)

y = [0.97,0.98,0.99,1,1.01,1.02,1.03,1.04,1.05,1.06]
axs[0].set_title("TDF hardness by 1st formula")
axs[0].plot(difficulty_dataframe.year, difficulty_dataframe.type1, marker='o')
axs[0].set_yticks(y)
axs[0].set_ylabel("hardness parameter")
axs[0].set_xticks(difficulty_dataframe.year)


axs[1].set_title("TDF hardness by 2nd formula")
axs[1].plot(difficulty_dataframe.year, difficulty_dataframe.type2, marker='o',color="red")
axs[1].set_yticks(y)
axs[1].set_ylabel("hardness parameter")
axs[1].set_xticks(difficulty_dataframe.year)


axs[2].set_title("TDF hardness by 3rd formula")
axs[2].plot(difficulty_dataframe.year, difficulty_dataframe.type3, marker='o', color="green")
axs[2].set_yticks(y)
axs[2].set_ylabel("hardness parameter")
axs[2].set_xticks(difficulty_dataframe.year)


figs.tight_layout(pad=0.5)
plt.show()