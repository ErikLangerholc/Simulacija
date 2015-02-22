import urllib.request


f = open("tickers.txt")
tickers = f.read().split(", ")
f.close()

for ticker in tickers:
    urllib.request.urlretrieve(
        "http://api.kibot.com/?action=history&interval=daily&startdate=10/1/2009&enddate=1/1/2015&username=guest&password=guest&symbol=" + ticker,
        "data\\" + ticker + ".txt")