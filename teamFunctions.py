# This file will contain functions that involve recording team OVR, and major stats including off rating, and def rating.
teamArr = ["New York Empire", "Indiana Overdrive", "Atlanta Talons", "Boston Charms", "Chicago Blues", "Washington Agents", "Miami Tides",
                "Detroit Drift", "Brooklyn Ballers", "Toronto Towers", "Philadelphia Founders", "Cleveland Gladiators", "Orlando Orbiters", 
                "Charlotte Stingers", "Milwaukee Spartans", "Los Angeles Stars", "New Orleans Airmen", "San Diego Surf", "Houston Cosmos", "Phoenix Firebirds", "Portland Roses",
                "San Francisco Quakes", "Utah Summit", "Denver Miners", "Minnesota Sabers", "Oklahoma City Outlaws", "San Antonio Sheriffs",
                "Dallas Knights", "Memphis Rockers", "Sacramento Royals"]

# When it comes to methods of measuring a teams greatness in Hoopland, I am rather limited.
def determineTeamRatings(team_df):
    # Make basic team metrics.
    for rows in team_df.itertuples(index=True, name='Pandas'):
        curTeam = team_df.iloc[rows[0]]
        offRtg = (curTeam['PTS'] + curTeam['OREB'] + curTeam['AST'] - curTeam['TO']) * curTeam['FG%'] * 0.01
        defRtg = curTeam['BLK'] + curTeam['STL'] + (curTeam['REB'] - curTeam['OREB']) - curTeam['PF']
        team_df.at[rows.Index, 'OFF'] =  offRtg
        team_df.at[rows.Index, 'DEF'] = defRtg
    return team_df

# a basic driver function that will run functions for determining team statistics.
def runTeamFunctions(team_df):
    t_df = determineTeamRatings(team_df)
    # print(t_df)
    listTeams(t_df)

# Will list out every franchise teams' major stats, in addition to rank.
def listTeams(t_df):
    print("{:^30} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} \t {:^5}".format("Team", "PTS", "AST", "STL", "BLK", "TO", "PF", "OFF", "DEF"))
    for row in t_df.itertuples(index=True, name='Pandas'):
        print("{:^30} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5} {:^5.2f} \t {:^5.2f}".format(t_df.at[row.Index, 'Team'], t_df.at[row.Index, 'PTS'], t_df.at[row.Index, "AST"], 
                                                                              t_df.at[row.Index, "STL"], t_df.at[row.Index, "BLK"], t_df.at[row.Index, "TO"], t_df.at[row.Index, "PF"], 
                                                                              t_df.at[row.Index, "OFF"], t_df.at[row.Index, "DEF"]))