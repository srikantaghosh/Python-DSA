## Normal Approach
# with open("/Applications/Ramos/Coding Repo/ProjectLord/venv/population_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

## Using Libraries tomread csvs

import csv

population_data = "/Applications/Ramos/Coding Repo/ProjectLord/venv/population_data.csv"
with open(population_data) as data_file:
    data= csv.reader(data_file)
    populatipn = []
    for row in data:
        if row[2] != "pop":
            populatipn.append(int(row[2]))
        
    print(populatipn)

## Here we would move to pandas! 

