#using panda
import matplotlib.pyplot as plt
import csv
with open ('fdata.csv',newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        print(','.join(row))
x=reader.index()
y=reader.index()
plt.show()
