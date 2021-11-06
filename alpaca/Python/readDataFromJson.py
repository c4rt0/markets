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

# Printing extracted data
for i in range(len(stockData)):
    t = datetime.fromtimestamp(stockData[i]["t"])
    o = stockData[i]["o"]
    c = stockData[i]["c"]
    h = stockData[i]["h"]
    l = stockData[i]["l"]
    v = stockData[i]["v"]
    day = t.strftime('%Y-%m-%d')
    print(i, "\n_________________ \nTime :", day)
    print("Open :", o)
    print("Close :", c)
    print("High :", h)
    print("Low :", l)
    print("Volume :", v, "\n")
