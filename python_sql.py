# import the sqlite3 python standard built-in libary
import sqlite3
import pandas as pd

# Using the library, set-up a connection between the python and the specified database
# using the database name or connection string.
# The connection acts as a bridge between the database and the current python instance
connection = sqlite3.connect("First.db")

# The cursor is the bus that travels the bridge and handles the querying of sql queries.
# The cursor object will allow us to execute queries and will return a list of tuples 
# containing all rows queried
conn_cursor = connection.cursor()

# cursor.execute will query the database and return a list of tuples for each rows
query_lst = conn_cursor.execute("SELECT * FROM <Sample Table>")

# Use cursor.executemany to execute multiple queries
# use question mark logic to add multiple rows
names = [("Vikram", "14", "Swimming"), ("Zhamba", "14", "Golf")]
conn_cursor.executemany("INSERT INTO <Sample Table> VALUES (?,?)", names)

# fetchone, fetchall, fetchmany will fetch the amount of rows in the list from cursor.execute
# fetchone will return one tuple, the rest will return a list of tuples.
first_row = query_lst.fetchone()
first_three_rows = query_lst.fetchmany(3)
all_rows = query_lst.fetchall()

#use pandas to create a dataframe for the rows you get back from a query
# using pd.read_sql_query, we pass through the query and the connection and it returns the 
# data in data frame rows and columns
data_frame = pd.read_sql_query("SELECT * FROM <Sample Table>", connection)


# On the other hand, you can return a data frame to a table using the df.to_sql() method
# pass in the table name and the connection to the database where the table will be created.
data_frame.to_sql("<Sample Table>", connection)



