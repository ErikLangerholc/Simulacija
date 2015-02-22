Potrebščine: Python 3.4

- Poskrbimo, da imamo v datoteki repozitorija tudi 2 prazni mapi "data" in "volatility".

- Prijavimo se v Kibot: gremo na link http://api.kibot.com/?action=login&user=guest&password=guest

- Zaženemo getdata.py. Počakamo, da program naloži podatke v mapo data. Za nekatere tickerje podatki obstajajo šele od nekega datuma naprej.

- Zaženemo volatility.py. To v mapo volatility naloži podatke o 3-mesečni volatilnosti.

- Zaženemo top25.py. Program ustvari to_buy.txt - tu notri so podatki, kdaj je treba kaj kupiti - kateri so v spodnjem decilu (ni jih vedno 25).

- Zaženemo simulacija.py. Ustvarjen je money.txt s podatki o našem finančnem stanju na dani datum. Prekopiramo v Excel.

Ker so tickerji iz ameriških borz, za benchmark vzamemo NASDAQ in Dow Jones. Tudi za začetni kapital bomo vzeli, da je 100 000$ in ne €.
Če bi imeli v €, bo po tečaju 1.1.2010 kupili $, trgovali z našo strategijo (ni učinka) in nato 1.1.2015 kupili €.
Tako bi se zaradi tečajne razlike naš kapital v € pomnožil z 1.188, kar pa je za naš izračun irelevantno.
Iz interneta naložimo podatke o teh dveh indexih in v excelu naredimo malo statistike.