dates = ['2010-01-04', '2010-02-01', '2010-03-01', '2010-04-01', '2010-05-03', '2010-06-01', '2010-07-01', '2010-08-02',
         '2010-09-01', '2010-10-01', '2010-11-01', '2010-12-01', '2011-01-03', '2011-02-01', '2011-03-01', '2011-04-01',
         '2011-05-02', '2011-06-01', '2011-07-01', '2011-08-01', '2011-09-01', '2011-10-03', '2011-11-01', '2011-12-01',
         '2012-01-03', '2012-02-01', '2012-03-01', '2012-04-02', '2012-05-01', '2012-06-01', '2012-07-02', '2012-08-01',
         '2012-09-04', '2012-10-01', '2012-11-01', '2012-12-03', '2013-01-02', '2013-02-01', '2013-03-01', '2013-04-01',
         '2013-05-01', '2013-06-03', '2013-07-01', '2013-08-01', '2013-09-03', '2013-10-01', '2013-11-01', '2013-12-02',
         '2014-01-02', '2014-02-03', '2014-03-03', '2014-04-01', '2014-05-01', '2014-06-02', '2014-07-01', '2014-08-01',
         '2014-09-02', '2014-10-01', '2014-11-03', '2014-12-01']

f = open("tickers.txt")
tickers = f.read().split(", ")
f.close()


def top_on_date(date):
    vols_on_date = []
    for ticker in tickers:
        f = open("volatility\\" + ticker + ".txt")
        text = f.read()
        f.close()
        lines = text.split("\n")
        if lines[-1] == "":
            lines = lines[:-1]
        l2 = [x.split(",") for x in lines]
        days = [x[0] for x in l2]
        vols = [float(x[1]) for x in l2]
        if date in days:
            vols_on_date.append((ticker, vols[days.index(date)]))
    vols_on_date.sort(key=lambda x: x[1])
    number_of_tickers = len(vols_on_date) // 10
    topvols = vols_on_date[:number_of_tickers]
    return [x[0] for x in topvols]

result = ""
for date in dates:
    a = ""
    for x in top_on_date(date):
        a += x + ","
    result += date + "," + a[:-1] + "\n"

f = open("to_buy.txt", "w")
f.write(result.rstrip())
f.close()