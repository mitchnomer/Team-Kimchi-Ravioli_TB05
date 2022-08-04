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

    loss = []

    for r in range(len(rows)):
        if r == 0:
            continue
        if rows[r][1] < rows[r-1][1]:
            temp = []
            temp.append("{:.2f}",format(float(rows[r][0])))
            temp.append("{:.2f}",format(forex*(int(rows[r-1][1]) - int(rows[r][1]))))

            loss.append(temp)
    
    return loss
    