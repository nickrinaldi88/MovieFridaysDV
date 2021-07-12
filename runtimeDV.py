import csv
from csv import reader
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

with open('MF.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    line_count = 0
    fields = ["Runtime", "Date"]
    with open('runtime.csv', 'w+') as runtime:
        writer = csv.writer(runtime)
        for row in reader:
            writer.writerow([row[2], row[3], row[6]])

thedata = pd.read_csv('runtime.csv', header=1)

print(thedata)

sns.set()
sns.scatterplot(x="Duration", y="Average", data=thedata)
plt.show()
