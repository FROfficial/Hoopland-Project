import pandas as pd
import csvFunctions
import teamFunctions

csv_file_list = csvFunctions.find_all_csv_files()

def findSeason(yr):
    index = (yr * 4) - 1
    df_t = pd.read_csv(csv_file_list[index])
    df_t = teamFunctions.runTeamFunctions(df_t)
    return df_t

def findPost(yr):
    index = (yr * 4) - 2
    df_t = pd.read_csv(csv_file_list[index])
    df_t = teamFunctions.runTeamFunctions(df_t)
    return df_t