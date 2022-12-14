#Profit and Loss
import csv
from pathlib import Path

def profitloss_function(forex):
    path = str(Path.cwd())
    path += '\csv_reports\PNL.csv'

    rows = []
    with open(path, 'r') as f:
        csvreader = csv.reader(f)
        next(csvreader)

        for row in csvreader:
            rows.append(row)

    loss = []

    for i in range(len(rows)):
        if i == 0:
            continue
        if rows[i][4] < rows[i-1][4]:
            temp = []
            temp.append("{:.2f}",format(float(rows[i][0])))
            temp.append("{:.2f}",format(forex*(int(rows[i-1][4]) - int(rows[i][4]))))

            loss.append(temp)
    
    return loss