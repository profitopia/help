Technik
#######

Profitopia wird von Eric Bergter, Niklas Fiedler, Jonas Hagge und Pascal Wichmann als Hobby-Projekt in der Freizeit entwickelt.

Programmierung
==============

Der Serverteil von Profitopia ist in Python geschrieben und verwendet das großartige Web-Framework `Django`_. Für die Datenbank nutzen wir eine PostgreSQL-Instanz.

Clientseitig nutzen wir JavaScript mit dem Framework `jQuery`_ für die Programmierung, HTML 5 für die Seitenstruktur und CSS 3 für das Design.

Die Kommunikation zwischen dem Spiel und dem Server findet nahezu ausschließlich mittels AJaX statt; diese Technik ermöglicht es, ohne das Neuladen einer Seite einzelne Anfragen an den Server zu senden, um so Daten abzurufen oder zu speichern. Dadurch ist für das Spielen nach der Anmeldung nur ein einzelner Seitenaufruf erforderlich; die weitere Kommunikation findet dann ausschließlich über AJaX statt. Das führt auch dazu, dass die Verzögerungen innerhalb des Spieles ziemlich gering sind, da keine vollständige Seite einschließlich der Daten, die sich niemals ändern (im Beispiel von Profitopia etwa die Accountinfo-Box oder die Navigation), geladen werden muss, sondern nur ganz explizit die Daten, die relevant sind; also etwa bei dem Laden eines Nutzerprofils nur die einzelnen Daten, nicht jedoch das Layout der Seite, die diese Daten anzeigen soll (da dies bereits beim initialen Seitenaufruf geladen wurde).

Für dieses Hilfe-Portal nutzen wir das Tool `Sphinx`_, das primär für das Dokumentieren von Softwareprojekten gedacht ist; durch kleinere Modifikationen im Template lässt es sich aber auch ideal für ein Hilfeportal, das sich an Endnutzer richtet, einsetzen. Einer der großen Vorteile von Sphinx liegt darin, dass statische HTML-Dateien generiert werden; damit ist keinerlei Serverseitige Interpretation der Sprachen erforderlich. Sicherheitstechnisch ist das natürlich optimal, da kein zusätzliches Potenzial für einen serverseitigen Exploit entsteht; darüber hinaus ist auch die Last, die entsteht, geringer.
Trotz dieser fehlenden serverseitigen Programmierung büßt Sphinx aber keinerlei Komfort ein; so gibt es etwa einen JavaScript-Suchindex, der eine Suche innerhalb dieser Hilfe ermöglicht.


Hosting
=======

Wir hosten Profitopia bei dem genialen Hoster `Uberspace`_, der neben allem für Webhosting erforderlichen noch deutlich mehr anbietet; etwa eine vollständige Linux-Shell (die insbesondere bei dem Betreiben eines Python-Projektes wie Profitopia äußerst hilfreich ist) und äußerst kompetenten Support, der innerhalb von kürzester Zeit antwortet.



.. _Django: https://www.djangoproject.com
.. _jQuery: http://jquery.com
.. _Sphinx: http://sphinx-doc.org
.. _Uberspace: https://uberspace.de
