import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics 
import csv
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

    

mean_list = []
for i in range(0,100):
    set_of_means = random_set_of_mean(30)
    mean_list.append(set_of_means)


mean = statistics.mean(mean_list)

print("mean of sampling distribution:- ",mean)

std_deviation = statistics.stdev(mean_list)

fig = ff.create_distplot([data],["student marks"], show_hist= False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.20], mode="lines", name="MEAN"))
fig.show()



first_std_deviation_start,first_std_deviation_end= mean-std_deviation, mean+std_deviation
second_std_deviation_start,second_std_deviation_end= mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end= mean-(3*std_deviation), mean+(3*std_deviation)
print("std1",first_std_deviation_start, first_std_deviation_end)
print("std2",second_std_deviation_start, second_std_deviation_end)
print("std3",third_std_deviation_start,third_std_deviation_end)


df = pd.read_csv("sample2.csv")
data = df["reading_time"].tolist()
mean_of_sample2 = statistics.mean(data)
print("mean of sample 2:- ",mean_of_sample2)
fig = ff.create_distplot([mean_list], ["reading_time"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[mean_of_sample2, mean_of_sample2], y=[0, 0.17], mode="lines", name="MEAN OF READING TIME"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.show()
