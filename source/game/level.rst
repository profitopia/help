Spiellevel
##########

Innerhalb des Spieles werden für verschiedene Aktionen Levelpunkte vergeben. Für eine vom Level abhängige Anzahl an Levelpunkten wird jeweils das nächste Level erreicht. Verschiedene Aktionen innerhalb des Spieles sind nur von dem Spiellevel abhängig möglich.

Aktionen
========

Für die folgenden Aktionen werden Levelpunkte vergeben:

+-------------------------------------------------------------------+---------------------+------------------------------+
| Aktion                                                            | Punktzahl           | Einschränkungen              |
+===================================================================+=====================+==============================+
| Login                                                             | 5 Punkte            | alle 12 Stunden              |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Abschluss des Tutorials                                           | 15 Punkte           | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erhalt einer Nachricht                                            | 5 Punkte            | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Versand einer Nachricht                                           | 5 Punkte            | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erstellung eines Profiltextes                                     | 10 Punkte           | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Wechsel der Stadt                                                 | 30 Punkte           | alle 7 Tage                  |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Spende an die Stadtkasse                                          | 5 Punkte            | alle 2 Tage                  |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erste Abstimmung bei der Bürgerschaftswahl                        | 15 Punkte           | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Sieg bei der Bürgermeisterwahl                                    | 150 Punkte          | keine                        |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Meldung eines Fehlers                                             | 25 Punkte           | keine                        |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erfindung einer Produktstufe                                      | 1 Punkt/Stufe       | keine                        |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Einstellung eines Mitarbeiters                                    | 50 Punkte           | keine                        |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Fortbildung eines Mitarbeiters                                    | 10 Punkte           | keine                        |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Gehaltserhöhung für einen Mitarbeiter                             | 5 Punkte            | alle 12 Stunden              |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Bau eines Gebäudes                                                | 30 Punkte           | keine                        |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Ausbau eines Gebäudes                                             | 10 Punkte           | keine                        |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erreichen eines Kapitals von 1 000 000 €                          | 75 Punkte           | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erreichen eines Kapitals von 1 000 000 000 €                      | 250 Punkte          | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erster Direktverkauf                                              | 100 Punkte          | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erster Direktankauf                                               | 100 Punkte          | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erster Marktverkauf                                               | 50 Punkte           | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erster Marktankauf                                                | 25 Punkte           | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+
| Erster Verkauf an den Großhändler                                 | 30 Punkte           | einmalig                     |
+-------------------------------------------------------------------+---------------------+------------------------------+


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
| variabel | höherer :ref:`buildings_upgrade` von Gebäuden                                                               |
+----------+-------------------------------------------------------------------------------------------------------------+
