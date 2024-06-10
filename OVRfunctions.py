import math

# Serves to displace the lowest Standard Deviation by identifying a minumum and adding its ABS+1
def RtgMin(array, avg):
    minval = 0
    for element in array:
        stdDev = math.sqrt((element - avg)**2 / (len(array)- 1))
        if (element - avg) < 0:
            stdDev *= -1
        stdDev = round(stdDev)
        if (stdDev < minval):
            minval = stdDev
        stdDev = minval*-1 + 1
    return (stdDev)

# Calls the displacement function for pts, and adds it to the actual deviation to get a 'overall'
def Rating(ply, avg, array):
    stdDev = math.sqrt((ply - avg)**2 / (len(array) - 1))
    if (ply - avg) < 0:
        stdDev *= -1
    stdDev = round(stdDev)
    stdDev += RtgMin(array,avg)
    return (stdDev)

# This is a general format which allows us to figure out ratings for a single stat.
def statOvr(ply, all, stat):
    player = round(ply[stat])
    maxLeague = round(all[stat].max())
    avgLeague = round(all[stat].mean())
    tempArray = [i for i in range(0,maxLeague)]
    return(Rating(player, avgLeague, tempArray)) 
