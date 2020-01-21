import pandas as pd


ncaa = pd.read_csv('NCAAData.csv')

for i in range(1985, 2020): 
    time_df = ncaa.loc[ncaa['Year'] == i]
    championship = time_df.loc[time_df['Stage'] == 'National Championship']
    team1 = championship['TeamOne']
    team2 = championship['TeamTwo']

    team1_score = int(championship['TeamOneScore'])
    team2_score = int(championship['TeamTwoScore'])

    if team1_score > team2_score: 
        winner = team1.values[0]
    else: 
        winner = team2.values[0]

    time_df2 = ncaa.loc[ncaa['Year'] == i + 1]

    returned = False
    for index, row in time_df2.iterrows():
        if row['TeamOne'] == winner or row['TeamTwo'] == winner:
            returned = True
            break

    if returned == True: 
        print(i, 'Winner Returned ', winner)
    else: 
        print(i, 'Winner Did NOT Return ', winner)
