# Import libraries 
import pandas as pd
from bs4 import BeautifulSoup
import requests
 
# Assign URL to variable
url = "https://www.codecademy.com/"
 
# Send request to download the data from URL
response = requests.request("GET", url)
 
# Create BeautifulSoup object
# Use HTML parser to parse the page's text
data = BeautifulSoup(response.text, 'html.parser')
 
# Print the first header of the page
print(data.html.h1)
 
# Instantiate list to append some content
content = []
 
# Use BeautifulSoup's find_all method to find all paragraph tags
words = data.find_all('p')
 
# Iterate through all paragraph tags
# append text to list with for loop
for word in words:
    content.append(word.text)
 
# Check content
print(content)
 
# Create dataframe of content with pandas DataFrame method
df = pd.DataFrame(content, columns= ['Text'])
 
# Check scraped dataframe
print(df)