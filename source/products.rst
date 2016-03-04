Produkte
########

Ein wesentlicher Teil des Spiels sind die Produkte, die in den entsprechenden Gebäuden produziert werden können.


Erfindungen
===========

Damit ein Produkt überhaupt produziert werden kann, muss es erfunden werden. Dies ist in der Produktübersicht unter Produkte->Erfindungen möglich.

Level
-----

Auch nach der ersten Erfindung können Produkte noch weiter verbessert werden, sodass diese ein höheres Level erreichen und insgesamt mehr Wert sind. Dabei kostet die Erfindung von Level 1 500 € und dauert eine Minute; jede Verbesserungs auf ein höheres Level kostet 16% mehr und dauert 10% länger als die Erfindung des jeweils vorherigen Levels. So kostet etwa die Erfindung von Level 50 ca. 720.131 € und dauert etwa eindreiviertel Stunden.

Limit
+++++

Produkte können maximal bis zum aktuellen Spielerlevel erfunden werden. Damit beträgt transitiv das maximal mögliche Level, bis zu dem ein Produkt erfunden werden kann, genau wie das Limit des Spielerlevels 100.

Produktübersicht
================

Die folgende Tabelle beinhaltet Informationen über alle Produkte, die derzeit in Profitopia existieren.

.. csv-table::
    :header: "Produkt", "Dauer", "Kosten", "Bedarf", "Gebäude", "Endprodukt"
    
    "Wasser", "0,3 Sekunden", "0,04 €", "*keiner*", "Brunnen", "nein"
    "Saat", "0,1 Sekunden", "0,20 €", "15 l Wasser", "Bauernhof", "nein"
    "Äpfel", "4,0 Sekunden", "2,00 €", "8 l Wasser; 0.1 kg Saat", "Bauernhof", "nein"
    "Birnen", "3,0 Sekunden", "1,50 €", "7 l Wasser; 0.1 kg Saat", "Bauernhof", "nein"
    "Orangen", "2,0 Sekunden", "2,50 €", "5 l Wasser; 0.1 kg Saat", "Bauernhof", "nein"
    "Silizium", "0,1 Sekunden", "8,00 €", "20 l Wasser", "Grundstofffabrik", "nein"
    "Transistor", "0,01 Sekunden", "0,00 €", "0.0001 kg Silizium", "Mikroelektronikfabrik", "nein"
    "Computerchip", "0,6 Sekunden", "0,03 €", "400 Stk Transistor", "Computerfabrik", "nein"
    "Prozessor", "20,0 Sekunden", "14,50 €", "2700 Stk Computerchip", "Computerfabrik", "nein"
    "RAM-Riegel", "3,0 Sekunden", "4,00 €", "250 Stk Computerchip", "Computerfabrik", "ja"
    "Computer", "05:00", "75,00 €", "2 Stk Prozessor; 4 Stk RAM-Riegel", "Computerfabrik", "ja"
    "Notebook", "30:00", "120,00 €", "1 Stk Prozessor; 2 Stk RAM-Riegel", "Computerfabrik", "ja"
    "Weintrauben", "3,5 Sekunden", "4,20 €", "2 l Wasser; 0.1 kg Saat", "Bauernhof", "nein"
    "Zuckerrübe", "7,6 Sekunden", "8,00 €", "10 l Wasser; 0.1 kg Saat", "Bauernhof", "nein"
    "Apfelsaft", "6,0 Sekunden", "1,70 €", "0.1 l Wasser; 0.9 kg Äpfel; 0.2 kg Zucker", "Getränkefabrik", "ja"
    "Birnensaft", "9,0 Sekunden", "2,00 €", "0.2 l Wasser; 0.7 kg Birnen; 0.05 kg Zucker", "Getränkefabrik", "ja"
    "Orangensaft", "11,0 Sekunden", "2,20 €", "0.05 l Wasser; 1.1 kg Orangen; 0.1 kg Zucker", "Getränkefabrik", "ja"
    "Rotwein", "45,0 Sekunden", "17,00 €", "0.2 l Wasser; 0.2 kg Weintrauben", "Getränkefabrik", "ja"
    "Weißwein", "52,0 Sekunden", "23,50 €", "0.25 l Wasser; 0.3 kg Weintrauben", "Getränkefabrik", "ja"
    "Zucker", "17,0 Sekunden", "9,50 €", "0.1 l Wasser; 2.3 kg Zuckerrübe", "Nahrungsmittelfabrik", "nein"

.. _selfcosts:

Selbstkosten
============

Die *Selbstkosten* eines Produktes sind die Kosten, die für die Produktion einer Einheit eines Produktes entstehen, wenn man das Produkt sowie alle dafür benötigten Zwischenprodukte (und deren Zwischenprodukte und so weiter) komplett selbst produziert. Daher geben die Selbstkosten nicht unbedingt die Kosten an, die man tatsächlich für dieses Produkt bezahlt hat.

Die Selbstkosten sind unter anderem für den Großhändler relevant, da dieser anhander der Selbstkosten den Preis berechnet, den er für ein Produkt bezahlt.
