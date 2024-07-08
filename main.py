  # #This program will calculate the averages, medians, and standard deviations
import math
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
  
df1 = pd.read_csv('Dataset1.csv')
df2 = pd.read_csv('Dataset2.csv')
df3 = pd.read_csv('Dataset3.csv')

# print(df1.columns)
# print(df2.columns) 
# print(df3.columns)  

####What is the average number of eliminations? (dataset1)
print("########## AVERAGE NUMBER OF ELIMINATIONS ##########")
                     ########DATASET1###########
dataset_file = 'Dataset1.csv'
data = pd.read_csv(dataset_file)
average_eliminations = data['Eliminations'].mean()

print(f"The average number of eliminations for DS1 is: {average_eliminations}")
                    ########DATASET2############
dataset_file = 'Dataset2.csv'
data = pd.read_csv(dataset_file)

average_eliminations_2 = data['Eliminations'].mean()
print(f"The average number of eliminations for DS2 is: {average_eliminations_2}")

                   #######DATASET3#########
dataset_file = 'Dataset3.csv'
data = pd.read_csv(dataset_file)
average_Solo_kills = data['Solo kd'].mean()


dataset_file = 'Dataset3.csv'
data = pd.read_csv(dataset_file)
average_Duo_kills = data['Duos kd'].mean()


dataset_file = 'Dataset3.csv'
data = pd.read_csv(dataset_file)
average_Trio_kills = data['Trios kd'].mean()


dataset_file = 'Dataset3.csv'
data = pd.read_csv(dataset_file)
average_Squads_kills = data['Squads kd'].mean()

                 ###ALL TOGETHER NOW###
All_Together_Now = average_Solo_kills + average_Duo_kills + average_Trio_kills + average_Squads_kills
All_Together_Now_2 = All_Together_Now / 4
print(f"The average number of eliminations for DS3 is: {All_Together_Now_2}")

Ultimate_Mean = ((All_Together_Now_2 + average_eliminations_2 + average_eliminations) / 3)
print(f"The average number of eliminations across all datasets is: {Ultimate_Mean}")



###What is the distribution of mental states (sober vs. high) during gameplay?
dataset_file = 'Dataset1.csv'
data = pd.read_csv(dataset_file)
state_counts = data['Mental State'].value_counts()
# Calculate the distribution as a percentage
distribution = state_counts / state_counts.sum() * 100
print("########## Distribution of Mental States ########## ")
print(distribution)

dataset_file_2 = 'Dataset2.csv'
data = pd.read_csv(dataset_file_2)
state_counts_2 = data['Mental State'].value_counts()
# Calculate the distribution as a percentage
distribution_2 = state_counts / state_counts.sum() * 100
print(distribution_2)

###What is the average accuracy of players?
print("########## AVERAGE ACCURACY ##########")
dataset_file = 'Dataset1.csv'
data = pd.read_csv(dataset_file)
average_accuracy = data['Accuracy'].mean()
new_average_accuracy = (average_accuracy * 100)
print("Average accuracy of players:", new_average_accuracy)

dataset_file = 'Dataset2.csv'
data = pd.read_csv(dataset_file)
data['Accuracy'] = data['Accuracy'].str.rstrip('%').astype(float)
average_accuracy = data['Accuracy'].mean()
print("Average Accuracy of players in DS2:", average_accuracy)

###HIGHEST SCORE
print("########### AVERAGE SCORE ###########")
dataset_file = 'Dataset3.csv'
data = pd.read_csv(dataset_file)
Average_solo_score_2 = data['Solo score'].mean()
print("Average solo score:", Average_solo_score_2)

###"Influencers"
print("########### Influencers ###########")
player_names = data['Player']
filtered_players = player_names[player_names.str.contains(r'Twitch|\.tv|YT', case=False)]
filtered_players_list = filtered_players.tolist()
print("Players with 'Twitch', '.tv', or 'YT' in their names:")
for player in filtered_players_list:
    print(player)


### Which player has the highest solo score?
print("########### HIGHEST SCORING PLAYERS###########")
dataset_file = 'Dataset3.csv'
data = pd.read_csv(dataset_file)
highest_solo_score = data['Solo score'].max()
player_with_highest_score = data.loc[data['Solo score'] == highest_solo_score, 'Player'].values[0]

print("Player with the highest solo score:", player_with_highest_score)
print("Highest solo score:", highest_solo_score)

### Average number of solo top 1  finished
print("######## Average solo top 1 finishes ########")
avg_finishes = df3[['Solo top1']].mean()
avg_finishes = avg_finishes.round()
print("Average solo top 1 finishes:", avg_finishes['Solo top1'])

### What is the win ratio for duos mode?
print("########## Average win ratio for duos ###########")
win_ratio = df3['Duos winRatio'].mean()
win_ratio = math.floor(win_ratio)
print('Average win ratio for duos:', win_ratio)

#What is the average minutes played in LTM (Limited Time Modes)?
print('####### Average Minutes Played in LTM #######')
ltm_minutes = df3['LTM minutesPlayed'].mean()
ltm_minutes = ltm_minutes.round(1)
print("Average minutes played on LTM:", ltm_minutes)

#Which player has the highest win ratio in LTM?



#Who has the highest overall KD (Kill-Death) ratio across all modes?
print("########## Highest overall KD###########")
dataset_file = 'Dataset3.csv'
data = pd.read_csv(dataset_file)
data['Total kills'] = data['Solo kills'] + data['Duos kills'] + data['Trios kills'] + data['Squads kills'] + data['LTM kills']
data['Total deaths'] = data['Solo matches'] - data['Solo top1'] + data['Duos matches'] - data['Duos top1'] + data['Trios matches'] - data['Trios top1'] + data['Squads matches'] - data['Squads top1']
#finds the top player overall :)
data['LTM matches'] - data['LTM top1']
data['KD ratio'] = data['Total kills'] / data['Total deaths']
#narrows it down even more. 
highest_kd_player = data.loc[data['KD ratio'].idxmax(), 'Player']
highest_kd_ratio = data['KD ratio'].max()
df10 = df3[(df3['Player'] == 'BH nixxxay')] 
deaths = (df10['Solo kills'] + df10['Duos kills'] + df10['Trios kills'] + df10['Squads kills'] + df10['LTM kills']) / (df10['Solo kd'] + df10['Duos kd'] + df10['Trios kd'] + df10['Squads kd'] + df10['LTM kd'])
kills = (df10['Solo kills'] + df10['Duos kills'] + df10['Trios kills'] + df10['Squads kills'] + df10['LTM kills'])
print(deaths)
print(kills)
print("The person with the highest KD ratio across all modes is:", highest_kd_player ,"\n" "with a KD ratio of:", highest_kd_ratio) 



### User with the longest username 
print('##### The player with the longest Username #####')
Longest_Playername = data['Player'].str.len().idxmax()
True_Longest_Playername = data.loc[Longest_Playername, 'Player']
print("User with the longest username:", True_Longest_Playername )


### Number of trios matches per player ###




  #mergedf = pd.merge(df1,df2)
#### Creating the graph ####

fig, axes = plt.subplots(2,2, sharey = True, sharex = True)
fig.suptitle("Matches for Each Mode")
sns.set_theme(style="ticks")

## Solos graph
avg = df3["Solo matches"].mean()
std = df3["Solo matches"].std()
axes[0,0].set_title("Solo Matches")
sns.histplot(ax = axes[0,0], x = df3['Solo matches'], color = "lightblue", edgecolor = "blue", kde = True)
axes[0,0].axvline(x = (avg + std), ymin = 0, ymax = df3['Solo matches'].max(), linestyle = "--", color = "green" )
axes[0,0].axvline(x = (avg - std), ymin = 0, ymax = df3['Solo matches'].max(), linestyle = "--", color = "green" )
axes[0,0].axvline(x = (avg), ymin = 0, ymax = df3['Solo matches'].max(), color = "black" )
axes[0,0].set_xlim([0,20000])

### Duos graph
avg = df3["Duos matches"].mean()
std = df3["Duos matches"].std()
axes[0,1].set_title("Duos Matches")
sns.histplot(ax = axes[0,1], x = df3['Duos matches'], color = "lightblue", edgecolor = "blue", kde = True )
axes[0,1].axvline(x = (avg + std), ymin = 0, ymax = df3['Duos matches'].max(), linestyle = "--", color = "green" )
axes[0,1].axvline(x = (avg - std), ymin = 0, ymax = df3['Duos matches'].max(), linestyle = "--", color = "green" )
axes[0,1].axvline(x = (avg), ymin = 0, ymax = df3['Duos matches'].max(), color = "black" )
axes[0,1].set_xlim([0,20000])

### Trios graph
avg = df3["Trios matches"].mean()
std = df3["Trios matches"].std()
axes[1,0].set_title("Trios Matches")
sns.histplot(ax = axes[1,0], x = df3['Trios matches'], color = "lightblue", edgecolor = "blue", kde = True )
axes[1,0].axvline(x = (avg + std), ymin = 0, ymax = df3['Trios matches'].max(), linestyle = "--", color = "green" )
axes[1,0].axvline(x = (avg - std), ymin = 0, ymax = df3['Trios matches'].max(), linestyle = "--", color = "green" )
axes[1,0].axvline(x = (avg), ymin = 0, ymax = df3['Trios matches'].max(), color = "black" )
axes[1,0].set_xlim([0,20000])

### Squads graph 
avg = df3["Squads matches"].mean()
std = df3["Squads matches"].std()
axes[1,1].set_title("Squad Matches")
sns.histplot(ax = axes[1,1], x = df3['Squads matches'], color = "lightblue", edgecolor = "blue", kde = True)
axes[1,1].axvline(x = (avg + std), ymin = 0, ymax = df3['Squads matches'].max(), linestyle = "--", color = "green" )
axes[1,1].axvline(x = (avg - std), ymin = 0, ymax = df3['Squads matches'].max(), linestyle = "--", color = "green" )
axes[1,1].axvline(x = (avg), ymin = 0, ymax = df3['Squads matches'].max(), color = "black" )
axes[1,1].set_xlim([0,20000])

### distance to materials

plt.show()

#Is there any correlation between kills and win ratio?



############################


####questions to ask (Dataset 3)###
#How many matches did each player play in trios mode?
#Which player has the most kills in squads mode?
#How many matches did each player play in each mode?
