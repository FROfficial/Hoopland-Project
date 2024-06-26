import teamFunctions
# Use this function to help determine the conference a player is in. (Used in conjunction to determine All-Star Status, and All-League Status')
def determineConference(ply_t):
    # Use arrays to determine whether a player plays in the East or West.
    eastArr = teamFunctions.teamArr[:15]
    westArr = teamFunctions.teamArr[15:30]

    # Comparisons
    for element in eastArr:
        if element == ply_t:
            return ("EAST")
    for element in westArr:
        if element == ply_t:
            return ("WEST")

# This function will iterate for all the functions that and determine every major team and award.
def calcAwards(ply_df):
    # All Star Teams:
    eastAS = []
    westAS = []

    # All-Hoopland Teams:
    allHoopFirst = []
    allHoopSecond = []
    allHoopThird = []

    # All-Defense Teams:
    allDefFirst = []
    allDefSecond = []
    allDefThird = []

    # Awards
    MVP_tracker = ply_df.iloc[0]
    DPOY_tracker = ply_df.iloc[0]
    ROTY_tracker = ply_df.iloc[0]
    sixMOTY_tracker = ply_df.iloc[0]
    Scoring_Champ = ply_df.iloc[0]
    Rebound_Champ = ply_df.iloc[0]
    Assists_Leader = ply_df.iloc[0]
    Steals_Leader = ply_df.iloc[0]
    Block_Champ = ply_df.iloc[0]

    for row in ply_df.itertuples(index=True, name= "Pandas"):
        # Current player
        curPly = ply_df.iloc[row[0]]
        # Calculate Regular Season Awards
        MVP_tracker = determineMVP(curPly, MVP_tracker)
        DPOY_tracker = determineDPOY(curPly, DPOY_tracker)
        ROTY_tracker = determineROTY(curPly, ROTY_tracker)
        sixMOTY_tracker = determineSixMOTY(curPly, sixMOTY_tracker)
        Scoring_Champ = determineChamp(curPly, Scoring_Champ, 'PTS')
        Rebound_Champ = determineChamp(curPly, Rebound_Champ, 'REB')
        Assists_Leader = determineChamp(curPly, Assists_Leader, 'AST')
        Steals_Leader = determineChamp(curPly, Steals_Leader, 'STL')
        Block_Champ = determineChamp(curPly, Block_Champ, 'BLK')
        
        # Calculate 'Team' Awards
        #   To be on the All-Star team you must first qualify to be considered
        if (allStarQualification(curPly)):
            # Determine which conference the player is in and add it to the array, anybody past index 15 will be erased once the loop ends.
            if (determineConference(curPly[1]) == "EAST"):
                eastAS.append(curPly)

            if (determineConference(curPly[1]) == "WEST"):
                westAS.append(curPly)

        #   To be on an All-Defense team you must first qualify to be considered
        if (allDefenseQualifications(curPly)):
            # Add any player that fits those requirements, later on I will partition the array into all 3 teams.
            allDefFirst.append(curPly)

        
        #   To be on an All-Hoopland team you must first qualify
        if (allHooplandQualifications(curPly)):
            allHoopFirst.append(curPly)

    # Sort the teams
    westAS.sort(key=lambda x: x['OVR'], reverse= True)
    eastAS.sort(key=lambda x: x['OVR'], reverse= True)
    allDefFirst.sort(key=lambda x: x['DEF'], reverse= True)
    allHoopFirst.sort(key=lambda x: x['DEF'] + x['OFF'], reverse=True)
    
    # Determine All-Defense and All-Hoopland Teams
    allDefSecond = allDefFirst[15:len(allDefFirst)]
    allDefThird = allDefSecond[30:len(allDefSecond)]
    allHoopSecond = allHoopFirst[15:len(allHoopFirst)]
    allHoopThird = allHoopSecond[30:len(allHoopSecond)]

    # Delete any players who did not make the cut.
    westAS[:] = westAS[:15]
    eastAS[:] = eastAS[:15]
    allDefFirst[:] = allDefFirst[:15]
    allDefSecond[:] = allDefSecond[:15]
    allDefThird[:] = allDefThird[:15]
    allHoopFirst[:] = allHoopFirst[:15]
    allHoopSecond[:] = allHoopSecond[:15]
    allHoopThird[:] = allHoopThird[:15]

    # pardon the long ass function call, this prints out the award winners in a formatted manner.
    printIndividualAwards(MVP_tracker, DPOY_tracker, ROTY_tracker, sixMOTY_tracker, Scoring_Champ, Rebound_Champ, 
                          Steals_Leader, Assists_Leader, Block_Champ)
    print("\n{:^80}".format("West All-Star Team"))
    printTeam(westAS)
    print("\n{:^80}".format("East All-Star Team"))
    printTeam(eastAS)
    print("\n{:^80}".format("All-Defense First Team"))
    printTeam(allDefFirst)
    print("\n{:^80}".format("All-Defense Second Team"))
    printTeam(allDefSecond)
    print("\n{:^80}".format("All-Defense Third Team"))
    printTeam(allDefThird)
    print("\n{:^80}".format("All-Hoopland First Team"))
    printTeam(allHoopFirst)
    print("\n{:^80}".format("All-Hoopland Second Team"))
    printTeam(allHoopSecond)
    print("\n{:^80}".format("All-Hoopland Third Team"))
    printTeam(allHoopThird)

    return (ply_df)

# Because Overall was designed to take into account defense, offense, WS, PER, and TS it is a great metric to determine who is the best.
def determineMVP(currentCandidate, reigningMVP):
    if (currentCandidate['OVR'] > reigningMVP['OVR']):
        return (currentCandidate)
    else:
        return (reigningMVP)

# This one is the most unique interms of awarding it. I need to consider STL, BLK, PF, and DREB.
# My best measure would be defensive rating like I did for the WS calc
def determineDPOY(currentCandidate, reigningDPOY):
    curDrtg = currentCandidate['STL'] + currentCandidate['BLK'] * 1.2 + (currentCandidate['REB'] - currentCandidate['OREB']) * 0.7 - currentCandidate["PF"]
    reignDrtg = reigningDPOY['STL'] + reigningDPOY['BLK'] * 1.2 + (reigningDPOY['REB'] - reigningDPOY['OREB']) * 0.7 - reigningDPOY['PF']
    if (curDrtg > reignDrtg):
        return currentCandidate
    else:
        return reigningDPOY

# Determine the champion/leader based on averages for any stat. A tie-breaker based on average minutes if stats averaged are the same.
def determineChamp(currentCandidate, reigningChamp, stat):
    if(currentCandidate[stat] > reigningChamp[stat]):
        return (currentCandidate)
    elif (currentCandidate[stat] == reigningChamp[stat]):
        # Little ternary action for the tie breaker if both averaged the same stats
        return currentCandidate if currentCandidate['MIN'] < reigningChamp['MIN'] else reigningChamp
    else:
        return (reigningChamp)

# This is similar to MVP with the stipulation that a player must only be new to the league. So their 'Year' value must be 'R'
def determineROTY(currentCandidate, reigningROTY):
    # Next Candidate Up Situation if you are not a rookie.
    if(reigningROTY['Year'] != 'R'):
        return currentCandidate
    # Should only happen if the reigning ROTY is a rookie, so if the candidate is not a rookie, they should not be able to take the award.
    if(currentCandidate['Year'] != 'R'):
        return reigningROTY
    # Determine the ROTY based on overall, and do a tie-breaker if needed.
    if (currentCandidate['OVR'] > reigningROTY['OVR']):
        return (currentCandidate)
    elif (currentCandidate['OVR'] == reigningROTY['OVR']):
        return currentCandidate if currentCandidate['MIN'] < reigningROTY['MIN'] else reigningROTY
    else:
        return (reigningROTY)

# This is very similar to ROTY, except this deals with the amount of minutes.
# For this specific award, I will say you cannot play more than 12 minutes and less then 45 games started.   
def determineSixMOTY(currentCandidate, reigningSixMOTY):
    if ((currentCandidate['MIN'] < 15 and currentCandidate['GS'] < 41) and (reigningSixMOTY['MIN'] < 15 and reigningSixMOTY['GS'] < 41)):
        if (currentCandidate['OVR'] < reigningSixMOTY['OVR']):
            return reigningSixMOTY
        elif (currentCandidate['OVR'] == reigningSixMOTY['OVR']):
            return currentCandidate if currentCandidate['MIN'] < reigningSixMOTY['MIN'] else reigningSixMOTY
        else:
            return currentCandidate
    elif (reigningSixMOTY['MIN'] < 15 and reigningSixMOTY['GS'] < 41):
        return reigningSixMOTY
    else:
        return currentCandidate

# Plain and simple, you must be at least 85 rated to be an All-Star
def allStarQualification(ply):
    if (ply[32] >= 85):
        return True
    return False

# You need at least a 5.5 defensive rating to be considered for All-Defense.
def allDefenseQualifications(ply):
    if (ply['DEF'] >= 5.5):
        return True
    return False

# You need to have a defensive + offensive rating of at least 10.5
def allHooplandQualifications(ply):
    if((ply['DEF'] + ply['OFF']) > 10.5):
        return True
    return False

# Print the award winners in a formated manner ~pretty
def printIndividualAwards (mvp, dpoy, roty, sixMoty, pts, reb, stl, ast, blk):
    print("{:<30} {:<30} {:<25} {:^8} {:^5} {:^7}".format("Award Name ", "Player Name", "Team", "Position", "Year", "Overall"))
    print("{:<30} {:<30} {:<25} {:^8} {:^5} {:^7}".format("Most Valuable Player ", mvp[0], mvp[1], mvp[2], mvp[3], mvp[32]))
    print("{:<30} {:<30} {:<25} {:^8} {:^5} {:^7}".format("Defensive Player of the Year ", dpoy[0], dpoy[1], dpoy[2], dpoy[3], dpoy[32]))
    print("{:<30} {:<30} {:<25} {:^8} {:^5} {:^7}".format("Rookie of the Year ", roty[0], roty[1], roty[2], roty[3], roty[32]))
    print("{:<30} {:<30} {:<25} {:^8} {:^5} {:^7}".format("Sixth Man of the Year ", sixMoty[0], sixMoty[1], sixMoty[2], sixMoty[3], sixMoty[32]))
    print("{:<30} {:<30} {:<25} {:^8} {:^5} {:^7}".format("Scoring Champion ", pts[0], pts[1], pts[2], pts[3], pts[32]))
    print("{:<30} {:<30} {:<25} {:^8} {:^5} {:^7}".format("Rebound Champion ", reb[0], reb[1], reb[2], reb[3], reb[32]))
    print("{:<30} {:<30} {:<25} {:^8} {:^5} {:^7}".format("Steals Leader ", stl[0], stl[1], stl[2], stl[3], stl[32]))
    print("{:<30} {:<30} {:<25} {:^8} {:^5} {:^7}".format("Assists Leader ", ast[0], ast[1], ast[2], ast[3], ast[32]))
    print("{:<30} {:<30} {:<25} {:^8} {:^5} {:^7}".format("Block Champion ", blk[0], blk[1], blk[2], blk[3], blk[32]))

# Used to print the members of an All Star Team
def printTeam (team):
    print("{:<30} {:<25} {:^8} {:^5} {:^7}".format("Player Name", "Team", "Position", "Year", "Overall"))
    for element in team:
        print("{:<30} {:<25} {:^8} {:^5} {:^7}".format(element['Player Name'], element['Team'], element['Position'], element['Year'], element['OVR']))
    
    print() # white space after it prints
