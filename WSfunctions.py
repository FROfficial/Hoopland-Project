# Series of Helper functions that specifically aid in calculating Win-Shares
# Every DataFrame is a modeled after generated spreadsheets. 
# [I acknowledge that I could very well make all of these 1 function that is overwritten, but I like the readability for this case in particular]

# returns the average Personal Fouls commited.
def AveragePF(dataFrame):
    return(dataFrame['PF'].mean())

# returns the average steals per game.
def AverageSTL(dataFrame):
    return (dataFrame['STL'].mean())

# returns the average blocks per game.
def AverageBLK(dataFrame):
    return (dataFrame['BLK'].mean())

# returns the average defensive rebounds per game by Subtracting Total Rebounds and Offensive Rebounds. 
def AverageDREB(dataFrame):
    return (dataFrame['REB'].mean() - dataFrame['OREB'].mean())

# returns the average +/- per game.
def AveragePlusMinus(dataFrame):
    return (dataFrame['+/-'].mean())

# returns the average points per game.
def AveragePTS(dataFrame):
    return(dataFrame['PTS'].mean())

# returns the total number of possesions.
def AveragePOS(dataFrame):
    return(dataFrame['FGA'].mean() + dataFrame['FTA'].mean() + dataFrame['TO'].mean() + dataFrame['AST'].mean())

