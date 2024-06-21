import OVRfunctions

# This file will contain functions that involve recording team OVR, and major stats including off rating, and def rating.
teamArr = ["New York Empire", "Indiana Overdrive", "Atlanta Talons", "Boston Charms", "Chicago Blues", "Washington Agents", "Miami Tides",
                "Detroit Drift", "Brooklyn Ballers", "Toronto Towers", "Philadelphia Founders", "Cleveland Gladiators", "Orlando Orbiters", 
                "Charlotte Stingers", "Milwaukee Spartans", "Los Angeles Stars", "New Orleans Airmen", "San Diego Surf", "Houston Cosmos", "Phoenix Firebirds", "Portland Roses",
                "San Francisco Quakes", "Utah Summit", "Denver Miners", "Minnesota Sabers", "Oklahoma City Outlaws", "San Antonio Sheriffs",
                "Dallas Knights", "Memphis Rockers", "Sacramento Royals"]

# a basic driver function that will run functions for determining team statistics.
def runTeamFunctions(team_df):
    t_df = determineTeamRatings(team_df)
    t_df = determineTeamRanks(t_df)
    listTeams(t_df)

# When it comes to methods of measuring a teams greatness in Hoopland, I am rather limited.
def determineTeamRatings(team_df):
    # Make basic team metrics.
    for rows in team_df.itertuples(index=True, name='Pandas'):
        curTeam = team_df.iloc[rows[0]]
        offRtg = (curTeam['PTS']* 1.2 + curTeam['OREB'] * 0.7 + curTeam['AST']) * curTeam['FG%'] * 0.01 - curTeam['TO'] * 2
        defRtg = curTeam['BLK'] * 2 + curTeam['STL'] * 2.2 + (curTeam['REB'] - curTeam['OREB']) * 0.7 - curTeam['PF'] * 1.5
        team_df.at[rows.Index, 'OFF'] =  offRtg
        team_df.at[rows.Index, 'DEF'] = defRtg
        team_df.at[rows.Index, 'OVR'] = (offRtg + defRtg)/2

    return team_df

# This will take a df and give offensive and defensive ranks based on their previously calculated ratings.
def determineTeamRanks(team_df):
    counter = 1
    team_df = team_df.sort_values(by='OFF', ascending=False)
    for rows in team_df.itertuples(index=True, name= 'Pandas'):
        team_df.at[rows.Index, 'O NO.'] = counter
        counter += 1
    
    counter = 1
    team_df = team_df.sort_values(by='DEF', ascending=False)
    for rows in team_df.itertuples(index=True, name= 'Pandas'):
        team_df.at[rows.Index, 'D NO.'] = counter
        counter += 1
    
    counter = 1
    team_df = team_df.sort_values(by='OVR', ascending=False)
    for rows in team_df.itertuples(index=True, name= 'Pandas'):
        team_df.at[rows.Index, 'OVR NO.'] = counter
        counter += 1
    return team_df

# Will list out every franchise teams' major stats, in addition to rank.
def listTeams(t_df):
    print("{:^30} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} \t {:^5} \t {:^5}".format("Team", "PTS", "AST", "STL", "BLK", "OFF-#", "DEF-#", "OVR-#", "OFF", "DEF"))
    for row in t_df.itertuples(index=True, name='Pandas'):
        print("{:^30} {:^5} {:^5} {:^5} {:^5} {:^5.0f} {:^5.0f} {:^5.0f} \t {:^5.2f} \t {:^5.2f}".format(t_df.at[row.Index, 'Team'], t_df.at[row.Index, 'PTS'], t_df.at[row.Index, "AST"], 
                                                                              t_df.at[row.Index, "STL"], t_df.at[row.Index, "BLK"], t_df.at[row.Index, "O NO."], t_df.at[row.Index, "D NO."], 
                                                                              t_df.at[row.Index, "OVR NO."], t_df.at[row.Index, "OFF"], t_df.at[row.Index, "DEF"]))