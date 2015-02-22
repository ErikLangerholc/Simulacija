def price_diff(ticker, date1, date2):
    """v procentih"""
    f = open("data\\" + ticker + ".txt")
    text = f.read().strip()
    f.close()
    lines = text.split("\n")
    dates = [x.split(",")[0] for x in lines]
    prices = [float(x.split(",")[4])for x in lines]
    price1 = prices[dates.index(reformat(date1))]
    price2 = prices[dates.index(reformat(date2))]
    return price2 / price1 - 1

def reformat(date):
    q = date.split("-")
    y, m, d = q[0], q[1], q[2]
    return m + "/" + d + "/" + y


money = [100000]

f = open("to_buy.txt")
text = f.read().strip()
f.close()
lines = text.split("\n")
dates = [x.split(",")[0] for x in lines]
dates.append("2014-12-31")
tickerlist = [x.split(",")[1:] for x in lines]

for i in range(len(tickerlist)):
    st_delnic = len(tickerlist[i])
    difflist = [price_diff(ticker, dates[i], dates[i+1]) for ticker in tickerlist[i]]
    money.append(money[-1] * (1 + sum(difflist) / st_delnic))

text = ""
for m in money:
    text += str(m) + "\n"
text += "\n"
for d in dates:
    text += d + "\n"

f = open("money.txt", "w")
f.write(text)
f.close()
