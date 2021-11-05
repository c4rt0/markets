import json
from datetime import datetime

# read file
dataFile = open('alpaca_aapl.json', 'r')
dataSet = dataFile.read()

# Parse the data
dataObject = json.loads(dataSet)
stockData = dataObject['AAPL']

# stockData is of type list...
# print(type(stockData))

# # Extracting individual elements: # #

# time...
for i in range(len(stockData)):
    t = datetime.fromtimestamp(stockData[i]["t"])
    day = t.strftime('%Y-%m-%d')
    print("Time :", day)
