# This file will take care of simplifying how we collect all the season csv files in the history of the league.
import os

# This function finds all csv contains in the project directory. This will be really useful in implementing self-refreshing statistics.
def find_all_csv_files():
    # To get an absolute path to the current folder.
    folder_path = os.path.abspath(os.getcwd())
    
    # Array used to keep all the file names.
    file_list = []

    # Walk through the directory
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".csv"):
                file_list.append(os.path.join(root, file))
    
    return file_list

# Starting in 2024, this function allows me to have a program that doesn't have hard coded year values.
def determineYear(file_list):
    size = len(file_list)
    return (size / 2) + 2023

# Create an array containing the list of all simulated years to facilitate self-refreshing options in the menu.
def listYears():
    # Figure out the number of years by using previously defined functions and a for loop.
    fileArr = find_all_csv_files()
    currentYear = determineYear(fileArr)
    yearsArr = [2024]
    if (currentYear != 2024):
        for i in range(2024, currentYear):
            yearsArr.append(i)
    # return the array
    return yearsArr