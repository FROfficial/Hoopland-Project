# Author: Fabian Ramirez
# Github: FROfficial

# Import Pandas for .csv support.
import pandas as pd

 
player_Sheet = "P_1950_season_stats.csv"
team_Sheet = "T_1950_season_stats.csv"

df = pd.read_csv(player_Sheet, header = 0).values

# Given a sheet, starting with "P" I want to calculate the following for each player:
#   Offensive Rating:
#       Should account for Points, Assists, Offensive Rebounds, and Turnovers

df = pd.read_csv(player_Sheet, usecols = ['PTS','OREB','AST','TO','TS%'], header = 0)

offensiveCalc = df['PTS'] * df['TS%'] * .01
offensiveCalc += df['OREB'] * 1.2
offensiveCalc += df['AST'] * 0.8
offensiveCalc -= df['TO']

#   Defensive Rating:
#       Should account for Steals, Blocks, Defensive Rebounds, and Personal Fouls

df = pd.read_csv(player_Sheet, usecols = ['STL','BLK','REB','OREB','PF'], header = 0)

defensiveCalc = df['STL'] * 2
defensiveCalc += df['BLK'] * 2.3
defensiveCalc += (df['REB'] - df['OREB']) * 1.2
defensiveCalc -= df['PF']


#   Overall Rating:
#       Add offensiveCalc , defensiveCalc, and small weight for Player Efficiency Rating (PER)

df = pd.read_csv(player_Sheet, header = 0)
overallCalc = offensiveCalc + defensiveCalc + df['PER'] * .1

# Using the calculated information add it to a df.
final_df = pd.concat([df,offensiveCalc],axis=1)
final_df = pd.concat([final_df,defensiveCalc],axis=1)
final_df = pd.concat([final_df,overallCalc],axis=1)
final_df.columns = ['Player Name','Team','Position','Year','GP','GS','MIN','PTS','FGM','FGA','FG%','3PM','3PA','3P%','FTM','FTA','FT%',
                   'REB','OREB','AST','STL','BLK','PF','TO','+/-','DD','TD','POTG','PER','TS%','EFG%','OFF','DEF','OVR']

print(final_df)
final_df.to_csv('1950_P_RS.csv',index=False)