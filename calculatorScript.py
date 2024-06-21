# This script handles all the calculation operations and creates a csv file for any files that are created.
# Given my fantasy league. I will use Win Shares, Player Efficiency Rating, and 
# Custom Offensive and Defensive Ratings to help determine awards and rating.

import pandas as pd
import WSfunctions
import OVRfunctions
import Awardfunctions
import teamFunctions

df_t = pd.read_csv("HL_2024_team_stats.csv", header = 0)
df_p = pd.read_csv("HL_2024_player_stats.csv", header = 0)

# function that will calculate win shares loosely based on the idea given by BasketBall Reference.
# additionally, the Defensive Win Shares part of the overall concept does not fit well with statistics
# provided by the auto-generated spreadsheets, so I am going to create my own measure of defensive rating.

# Calculate the custom formula for Win-Shares
def calcWS(player, league, team, allPlayers):
    # Calculate Player Points Produced: GP * PTS
    pointsProduced = player['GP']*player['PTS']

    # Calculate Player Possessions: FGA + FTA + TO + AST
    possesions = player['FGA']+player['FTA']+player['TO']+player['AST']   

    # Calculate Marginal Offense: 
    MO = pointsProduced - 0.92 * WSfunctions.AveragePTS(allPlayers) * possesions

    # Calculate Marginal Points Per Win:
    MPW = 0.32 * WSfunctions.AveragePTS(league) * (WSfunctions.AveragePOS(team)/WSfunctions.AveragePOS(league))
    
    # Calculate Offensive Win Shares: Marginal Offense / Marginal Points Per Win.
    OFF_WS = MO/MPW
    
    # Calculate Defensive Value: most important stats when considering defense is STL, BLK, DREB, +/-, and PF
    DV = (player['STL'] / WSfunctions.AverageSTL(allPlayers)) * 20 
    DV += (player['BLK'] / WSfunctions.AverageBLK(allPlayers)) * 22 
    DV += ((player['REB']-player['OREB']) / WSfunctions.AverageDREB(allPlayers)) * 12
    DV += player['+/-'] - WSfunctions.AveragePlusMinus(allPlayers) - player['PF']
    DV *= ((player['GP'] * player ['MIN'])/(82*24))
    
    # - Pardon the chunk. Then finally calculate a very concise version of WS.
    WS = DV+OFF_WS
    WS /= player['GP']
    return(WS)

# Calculate Overall using metrics such as PER, WS, and all major stats.
def calcOVR(player, allPlayers):
    # Calculate Offensive Rating
    oRtg = OVRfunctions.statOvr(player, allPlayers, 'PTS') * 1.2 + OVRfunctions.statOvr(player, allPlayers, 'OREB') * 0.7
    oRtg += OVRfunctions.statOvr(player, allPlayers, 'AST') * 0.8 - player['TO']

    # Calculate Defensive Rating
    dRtg = OVRfunctions.statOvr(player, allPlayers, 'STL') + OVRfunctions.statOvr(player, allPlayers, 'BLK') * 1.2
    dRtg += OVRfunctions.statOvr(player, allPlayers, 'REB') * 0.7 - player['PF']

    # Calculate Reliability Rating : based on true shooting and minutes.
    rRtg = round(OVRfunctions.statOvr(player, allPlayers, 'TS%') + OVRfunctions.statOvr(player, allPlayers, 'MIN') * 0.5)

    # Calculate Overall. (value added at the end is arbitrary, just to fit the uniform values of things such as 2K)
    rtg = round(oRtg + dRtg + OVRfunctions.statOvr(player, allPlayers, 'PER') + rRtg + OVRfunctions.statOvr(player, allPlayers, 'WS')) + 58
    if (rtg > 99):
        # For those crazy players who might break the scale
        rtg = 99
    return [rtg, oRtg, dRtg]

# Find at what index the team ended up in for the team dataframe.
def searchTeamIndex(plyTeam, team_df):
    index = 0 
    for row in team_df.itertuples(index=True, name= "Pandas"):
        if row[1] == plyTeam:
            index = row[0]
    return index

# WSvals will create an array with every WS so I can use the statOVR function and later add it player dataframe.
def WSvals(player_df, team_df):
    for row in player_df.itertuples(index=True, name= 'Pandas'):
        # Find the team index for each player according to the team dataframe.
        t_index = searchTeamIndex(row[2], team_df)
        
        # Calculate WS
        plyWS = calcWS(player_df.iloc[row[0]], team_df, team_df.iloc[t_index], player_df)

        # Add the WS value at the correct index. (* this is the only way I could get it to work)
        player_df.at[row.Index, 'WS'] = plyWS            
    return (player_df)

# Calculate every players overall, def rating, and off rating and add it to the dataframe and return that.
def calcAllOVRs(player_df):
    for row in player_df.itertuples(index=True, name= "Pandas"):
        plyOVR = calcOVR(player_df.iloc[row[0]], player_df)
        player_df.at[row.Index, 'OVR'] = plyOVR[0]
        player_df.at[row.Index, 'OFF'] = plyOVR[1]
        player_df.at[row.Index, 'DEF'] = plyOVR[2]
    return (player_df)

def printPlayerInfo(df):
    # The Header
    print("{:<28} {:<28} {:<5} {:<5}".format("Player Name", "Team", "Year","OVR"))
    
    # Print out each formatted row.
    for row in df.itertuples(index=True, name="Pandas"):
        print("{:<28} {:<28} {:<5} {:<5}".format(df.at[row.Index, 'Player Name'], df.at[row.Index, 'Team'], df.at[row.Index, 'Position'], df.at[row.Index, 'OVR']))



nu_df = WSvals(df_p, df_t)
nu_df = calcAllOVRs(nu_df)
nu_df = nu_df.sort_values(by='OVR', ascending=False)
#nu_df = Awardfunctions.calcAwards(nu_df)

#printPlayerInfo(nu_df)

teamFunctions.runTeamFunctions(df_t)

#   -   Test Calls:    - (* some function definitions may have changed)
# calcOVR(calcWS(temp_player, df_t, temp_team, df_p), temp_player, df_p)
# calcWS(temp_player, df_t, temp_team, df_p)
# print(OVRfunctions.Team.ATLANTA_TALONS.value)
# searchTeamIndex("Atlanta Talons", df_t)
# Awardfunctions.determineConference(nu_df.iloc[7][1])
