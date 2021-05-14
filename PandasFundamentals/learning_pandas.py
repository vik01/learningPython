import numpy as np
import pandas as pd

# Pandas is a very useful data managing library
# Two pandas objects: series and dataframes
#   Series are essentially a numpy array but they can be indexed by other things besides numbers 
#       e.g. you can index a Series by a name or an alpha-numeric sequence
#   Dataframes are like tables with columns of similar data (series) and rows of similar records

# generic indexing through numbers of a series
ages = np.array([19, 18, 20, 19])
pandas_series_num = pd.Series(ages)
print(pandas_series_num)

# indexing through names of a Series
pandas_series_names = pd.Series(ages, index=["Vikram", "Cuthbert", "Michael", "Peter"])
print(pandas_series_names)

#NOTE: once a series is printed to the console, the data type of the element is also printed

# A Dataframe can be created through multiple methods such as csv files, sql queries (see python_sql.py), python lists, or python dictionaries

# Below is an example of a data frame from a python list
dataf = pd.DataFrame([["Vikram", 19], ["Cuthbert", 18], ["Peter", 20], ["Michael", 19]], columns=["Name", "Ages"])

# Below is an exaple of a dataframe from a dictionary
dataf_two = pd.DataFrame({"Name": ["Vikram", "Cuthber", "Peter", "Michael"], "Age": [19, 18, 20, 19]})

# Below is an example of changing a csv to a dataframe 
dataf_from_csv = pd.read_csv("files\\logger.csv")
dataf_from_larger_csv = pd.read_csv("files\\movies.csv")

# Column names at the top, rows on the side
print(f"From list: {dataf}")
print(f"From dictionary: {dataf_two}")
print(f"From csv: {dataf_from_csv}")

# Can also index by specific rows
dataf.set_index("Name")
dataf_two.set_index("Name")

# Now you will see that the numbers on the left side are gone 
print(f"""From list after setting index to name: 
{dataf}""")
print(f"From dictionary: {dataf_two}")


# You can use head() to get the first couple of entries in a large dataframe and info() to get the information of a large data frame.
print(dataf_from_larger_csv.head()) 
print(dataf_from_larger_csv.info())

# You can select certain columns from a dataframe using two methods (using dataf dataframe):
select_method_one = dataf["Name"]
select_method_two = dataf.Name
# When selecting one column from a dataframe, you get back a Series Object 
print(f"First method of selecting column from dataframe: {select_method_one}")
print(f"Second method of selecting column from dataframe: {select_method_two}")

# You can also select multiple columns which will be saved to a dataframe variable:
select_multiple_columns = dataf[["Name", "Ages"]]
print(f"Selecting multiple columns {select_multiple_columns}")

# You can select rows by using indexes, which start at 0 end at len() - 1
select_row_two = dataf.iloc[1]
print(f"Second Row: {select_row_two}")