import csv
import plotly.express as px
import numpy as np

#with open("Size of TV,_Average time spent watching TV in a week (hours).csv") as csv_file:
    #df=csv.DictReader(csv_file)
    #fig=px.scatter(df,x="Size of TV",y="\tAverage time spent watching TV in a week (hours)")
    #fig.show()

def getDataSource(data_path):
    size_of_tv=[]
    avg_time_spent=[]
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            avg_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return{"x" :size_of_tv, "y" :avg_time_spent}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("correlation btw Size of TV and average time spent watching TV in a week: \n--->",correlation[0,1])

def setup():
    data_path = "Size of TV,_Average time spent watching TV in a week (hours).csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()