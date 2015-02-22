from datetime import *
from statistics import pstdev
from math import log


def get_volatility(ticker):
    f = open("data\\" + ticker + ".txt")
    content = f.read().strip()
    f.close()
    lines = content.split("\n")
    dateprice = [(date(int(x[0][-4:]), int(x[0][:2]), int(x[0][3:5])), float(x[4])) for x in [x.split(",") for x in lines]] #list tuplov (date, price)
    firsts = first_of_the_month(dateprice)
    if firsts[0].day <= 5:
        firsts = firsts[3:]
    else:
        firsts = firsts[4:]

    result = ""
    for tradeday in firsts:
        population = []
        for dayy, price in dateprice:
            if tradeday - dayy < timedelta():
                break
            elif tradeday - dayy <= timedelta(days=90):
                population.append(price)
        result += str(tradeday) + "," + str(vol(population)) + "\n"
    result = result.rstrip()
    f = open("volatility\\" + ticker + ".txt", "w")
    f.write(result)
    f.close()




def first_of_the_month(dateprice):
    """seznam dni ki so prvi v mesecu"""
    r = []
    dates = [x[0] for x in dateprice]
    r.append(dates[0])
    for d in dates:
        if d.month != r[-1].month:
            r.append(d)
    return r

def vol(s):
    logreturns = [log(s[i+1] / s[i]) for i in range(len(s) - 1)]
    return pstdev(logreturns) * 252**0.5




f = open("tickers.txt")
tickers = f.read().split(", ")
f.close()

for ticker in tickers:
    get_volatility(ticker)