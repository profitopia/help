Spiellevel
##########

Innerhalb des Spieles werden für verschiedene Aktionen Levelpunkte vergeben. Für eine vom Level abhängige Anzahl an Levelpunkten wird jeweils das nächste Level erreicht. Verschiedene Aktionen innerhalb des Spieles sind nur von dem Spiellevel abhängig möglich.

Aktionen
========

Für die folgenden Aktionen werden Levelpunkte vergeben:

todo

Notwendige Levelpunkte
======================

Die für das Erreichen eines höheren Levels erforderlichen Levelpunkte bestimmen sich durch die Funktion :math:`f(x) = 15 \cdot 1,05^x + 0,2x^2 + 15x + 150` für :math:`\{x \in \mathbb{Z} | 1 \le x \le 99 \}`

Dabei wird der von der Funktion zurückgegebene Wert gerundet. Folglich sind zum Erreichen von Level 100 insgesamt 193907 Levelpunkte erforderlich.

Aufgrund des vorliegenden enthaltenen exponentiellen Wachstums steigt die benötigte Zahl an Levelpunkten proportional zum Level an.

Beim Erreichen von Level 100 werden weitere Levelpunkte zwar noch im Verlauf gespeichert, haben jedoch keine weiteren Auswirkungen auf das Spiellevel.

Freischaltbare Funktionen
=========================

Durch das Erreichen von höheren Leveln werden verschiedene Funktionen freigeschaltet. Im Folgenden sind diese aufgelistet:

+----------+-------------------------------------------------------------------------------------------------------------+
| Level    | Freigeschaltete Funktion                                                                                    |
+==========+=============================================================================================================+
| 2        | Kandidatur zur :ref:`city_mayor_election`                                                                   |
+----------+-------------------------------------------------------------------------------------------------------------+
| 3        | :ref:`trade_immediate_sell`                                                                                 |
+----------+-------------------------------------------------------------------------------------------------------------+
| variabel | höhere :ref:`employees_training`                                                                            |
+----------+-------------------------------------------------------------------------------------------------------------+
