import pandas as pd

# variable holding the amount of rows you want
amount = 10

# create a Pandas DataFrame from Sunspots.csv
sunspots_df = pd.read_csv("Sunspots.csv")

# get the most recent data by selecting the last 10 rows
recent_sunspots = sunspots_df.tail(amount)

# calculate the mean
avg = sum(recent_sunspots["Monthly Mean Total Sunspot Number"]) / len(recent_sunspots["Monthly Mean Total Sunspot Number"])

# use DataFrame method to produce mean
total_mean = recent_sunspots["Monthly Mean Total Sunspot Number"].mean()

# create lists for adding a mean and level column to the DataFrame
mean_list = []
level = []

# iterate through list and append mean
for i in range(amount):
    mean_list.append(total_mean)

# iterate through "Monthly Mean Total Sunspot Number" column of the DataFrame
for x in recent_sunspots["Monthly Mean Total Sunspot Number"]:

    # add conditionals
    if x > total_mean:
        level.append("High")
    if x < total_mean:
        level.append("Low")
    if x == total_mean:
        level.append("Flat")

# insert lists as columns into the DataFrame
recent_sunspots.insert(3, "level", level)
recent_sunspots.insert(4, "mean", mean_list)

# print results
print(recent_sunspots)

# get min and max values
print(recent_sunspots["Monthly Mean Total Sunspot Number"].min())
print(recent_sunspots["Monthly Mean Total Sunspot Number"].max())

# convert to dictionary and assign it to a variable
recent_sunspots_dict = recent_sunspots.to_dict()
print(recent_sunspots_dict)

# inspect the DataFrame more
print(recent_sunspots.info())





