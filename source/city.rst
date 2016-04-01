Städte
######

In Profitopia gibt es Städte, die Zusammenschlüsse von mehreren Spielern sind. Jeder Spieler gründet bei der Registrierung eine eigene Stadt. Später kann er sich dann bei anderen Städten bewerben, um diesen beitreten zu können, oder andere Spieler motivieren, sich in der eigenen Stadt zu bewerben. Es ist zwar auch möglich, alleine in einer Stadt zu sein, allerdings lässt ein Spieler sich dadurch diverse Vorteile entgehen, die eine Stadt mit sich bringt.

Bürgermeister
=============

Eine Stadt kann einen Bürgermeister haben, der gewählt wird. Dieser hat diverse Möglichkeiten hinsichtlich der Stadt, so kann er

* Bewerbungen von Spielern annehmen oder ablehnen,
* Einwohner aus der Stadt werfen,
* das Stadtprofil bearbeiten,
* stadtinterne Mitteilungen anderer Spieler löschen und
* alle Entscheidungen hinsichtlich der Infrastruktur treffen.

.. _city_mayor_election:

Bürgermeisterwahl
-----------------

Der Posten des Bürgermeisters wird durch eine Wahl besetzt. Diese findet in regelmäßigen Abständen statt, sofern die Voraussetzungen erfüllt sind. In Städten, die einen Bürgermeister haben, findet die Wahl zehn Tage nach der vorherigen Wahl statt; hat die Stadt aktuell keinen Bürgermeister, etwa weil sie gerade erst gegründet wurde oder der vorherige Bürgermeister die Stadt verlassen hat, findet die erste Wahl zwei Stunden nach der Gründung beziehungsweise dem Verlassen der Stadt statt.

Damit ein Einwohner als Kandidat für die Wahl gilt, muss er in der entsprechenden Legislaturperiode (also seit der letzten Wahl) mindestens 50 € gespendet haben.

Für das Stattfinden einer Wahl gibt es zwei Voraussetzungen:

* Es muss mindestens einen kandidierenden Einwohner in der Stadt geben (der also die zuvor genannten Voraussetzungen für die Kandidatur erfüllt) und
* Die Stadt muss über mindestens 500 € verfügen, da dies die Gebühr für die Durchführung der Wahl ist.

Sollten diese Bedingungen nicht erfüllt sein, wird die Wahl um einen Tag verschoben und die Bedingungen dann erneut überprüft. Die Dauer dieser Verschiebung ist dabei unabhängig davon, ob die Stadt einen Bürgermeister hat oder nicht.

Infrastruktur
=============

Eine Stadt besitzt eine Infrastruktur, die verbessert werden kann. Dadurch bringt sie der Stadt und den Einwohnern verschiedene Vorteile. Die Infrastruktur der Stadt besteht aus verschiedenen Komponenten, die in der folgenden Tabelle aufgeführt sind.

Infrastrukturkomponenten können haben einen Fertigstellungsgrad, durch den beeinflusst wird, wie stark der Vorteil der entsprechenden Infrastrukturkomponente wirkt.

Infrastrukturkomponenten
------------------------

Die folgenden Infrastrukturkomponenten existieren in Profitopia. Die Kosten geben dabei jeweils die Gebühr für einen Prozentpunkt an (siehe unten für weitere Details).

+-------------------------+---------------------------------------+---------------------+----------------------------+-------------------+
| Infrastrukturkomponente | Funktion                              | Vorteil/Limitierung | Anfangsfertigstellungsgrad | Grundkosten       |
+=========================+=======================================+=====================+============================+===================+
| Stadtfläche             | Durch die Stadtfläche wird die        | je 4% ermöglichen   | 20%                        | 10.000 €          |
|                         | Kapazität einer Stadt festgelegt.     | einen Einwohner     |                            |                   |
+-------------------------+---------------------------------------+---------------------+----------------------------+-------------------+
| Markt-Rahmenvertrag     | Senkung der Marktprovision            | je 0,5% geringere   | 0%                         | 50.000 €          |
|                         |                                       | Provision           |                            |                   |
+-------------------------+---------------------------------------+---------------------+----------------------------+-------------------+
|Großhändler-Rahmenvertrag| Erhöhung der Erlöse durch den         | je 0,5% höhere      | 0%                         | 50.000 €          |
|                         | Großhändler                           | Bezahlung           |                            |                   |
+-------------------------+---------------------------------------+---------------------+----------------------------+-------------------+
| Freizeiteinrichtungen   | Höhere Effizienz der Mitarbeiter      | je 0,3% höhere      | 0%                         | 75.000 €          |
|                         |                                       | Effizienz           |                            |                   |
+-------------------------+---------------------------------------+---------------------+----------------------------+-------------------+

Markt-Rahmenvertrag
+++++++++++++++++++

Der Markt-Rahmenvertrag senkt die Marktprovision, die beim Aufkauf oder dem Zurückziehen eigener Marktposten anfällt. Die maximal mögliche Senkung beträgt 50% (100 * 0,5%), sodass statt den ursprünglichen 25% nur noch 12,5% fällig werden.

Großhändler-Rahmenvertrag
+++++++++++++++++++++++++

Der Großhändler-Rahmenvertrag erhöht die Bezahlung des Großhändlers um je 0,5%. Der maximal mögliche Bonus beträgt 50%.

Freizeiteinrichtungen
+++++++++++++++++++++

Die Freizeiteinrichtungen ermöglichen den Mitarbeitern zusätzliche Entspannung während des Feierabends, sodass sie während der Arbeitszeit eine höhere Motivation aufweisen.

Fertigstellungskosten
---------------------

Für die Verbesserung von Infrastrukturkomponenten entstehen Kosten, die die Stadt mit ihrem Kapital finanzieren muss. Diese Kosten steigen mit dem Fertigstellungsgrad der entsprechenden Komponente.

Die Fertigstellung erfolgt in ganzen Prozentpunkten. Dabei wird für jeden Prozentpunkt, um den die Infrastrukturkomponente verbessert werden soll, der Preis mit dem neuen Prozentwert multipliziert (als Zahlen- und nicht als Prozentwert).

*Beispiel*: Die Stadtfläche (Die Grundkosten betragen 10.000 €) soll auf einen Fertigstellungsgrad von 50 % erweitert werden. Dadurch entstehen Kosten in Höhe von :math:`50 \cdot 10\,000\text{ €} = 500\,000\text{ €}`. Für die vollständige Fertigstellung (die bei einem Anfangsfertigstellungsgrad von 20% beginnt) entstehen also insgesamt Kosten in Höhe von 48.400.000 €.

Neben den finanziellen Kosten besteht als zusätzliche Voraussetzung für die Verbesserung der Infrastruktur eine erforderliche Zahl an Einwohnern. Insgesamt kann eine Stadt bei Fertigstellung der Stadtfläche 25 Einwohner haben. Der Anteil an Einwohnern einer Stadt von dem insgesamt maximal möglichen Anteil entspricht dem maximal möglichen Fertigstellungsgrad der einzelnen Infrastrukturkomponenten. Hiervon ausgenommen ist allerdings die Stadtfläche, da es andernfalls nicht möglich wäre, diese Voraussetzung zu erfüllen.

Pro Stunde kann nur eine einzige Infrastrukturkomponente verbessert beziehungsweise fertiggestellt werden. Pro Aktion ist jeweils nur eine Verbesserung um einen Prozentpunkt möglich.
