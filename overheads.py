Overheads
import csv
from pathlib import Path

def profitloss_function(forex):
    path = str(Path.cwd())
    path += '\csv_reports\COH.csv'

    rows = []
    with open(path, 'r') as f:
        csvreader = csv.reader(f)
        next(csvreader)

        for row in csvreader:
            rows.append(row)
    
    max = 0
    maxOverheads = [] #list which returns [max overhead, what overhead]

    for r in range(len(rows)):
        if max < float(rows[r][1]):
            max = float(rows[r][1])
            maxOverheads = [rows[i][0], "{:.2f},format(max * forex")]

    return maxOverheads