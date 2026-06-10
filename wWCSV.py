import requests
import pandas as pd
from io import StringIO

# using csv file
pd.read_csv('healthcare_dataset.csv')

#opening a csv file using url
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
# url = ""
# u cn change url as per ur  need very helpful code snippet
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; RV.66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)

pd.read_csv(data)

# using sep parameter
pd.read_csv('file.tsv', sep='\t')