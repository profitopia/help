Großhändler
###########

Der Großhändler kauft Endprodukte an, für die er einen vom Level und der verkauften Menge abhängigen Preis bezahlt.

Bezahlung
=========

Die Bezahlung des Großhändlers ist abhängig von den :ref:`selfcosts` des Produktes, der Dauer der Produktion des Produktes und aller Zwischenprodukte, dem Level und der Menge an Einheiten, die in einer Transaktion an den Großhändler verkauft werden. Dabei wächst die Bezahlung mit dem Produktlevel und der Menge; bei besonders kleinen Mengen führt der Verkauf an den Großhändler möglicherweise sogar zu Verlusten, sodass es erforderlich sein kann, mit anderen Spielern Handel zu betreiben, um eine ausreichend große Menge in einer Transaktion verkaufen und damit einen maximalen Gewinn erwirtschaften zu können.

Konkret berechnet sich der Preis, den der Großhändler zahlt, mit der folgenden Formel, wobei p der Selbstkosten-Wert, l das Produktlevel, n die verkaufte Menge und d die Summe der Dauer von dem Produkt und allen Zwischenschritten ist:

:math:`p \cdot \log_3(n + 1) \cdot (\frac{1,0235310219^{\frac{l-1}{2}}}{7} + 0,00002 \cdot d)`

Limitierung
===========

Es können maximal 50 Millionen Produkte pro Spieler und Stunde an den Großhändler verkauft werden. Damit ist auch das Limit einer einzelnen Transaktion auf 50 Millionen Produkte beschränkt.

Ein Beispiel für die Berechnung der Limitierung:

1. Verkauf von 10 Millionen Endprodukten um 10:00
2. Verkauf von 5 Millionen Endprodukten um 10:15
3. Verkauf von 35 Millionen Endprodukten um 10:30

Damit ist das Limit des Großhändlers nach der Transaktion um 10:30 erschöpft. Um 11:00, also eine Stunde nach der ersten Transaktion, werden wieder 10 Millionen Einheiten frei, da die erste Transaktion dann nicht mehr in das Zeitfenster der letzten Stunde fällt. Sollte keine weitere Transaktion stattfinden, können aber 11:15 wieder 15 Millionen und ab 11:30 wieder die vollständigen 50 Millionen Einheiten verkauft werden.
