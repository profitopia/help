Technik
#######

Profitopia wird von Stefan Tarnowski und Pascal Wichmann als Hobby-Projekt in der Freizeit entwickelt.

Programmierung
==============

Der Serverteil von Profitopia ist in Python geschrieben und verwendet das großartige Web-Framework `Django`_. Für die Datenbank nutzen wir eine PostgreSQL-Instanz.

Clientseitig nutzen wir JavaScript mit dem Framework `jQuery`_ für die Programmierung, HTML 5 für die Seitenstruktur und CSS 3 für das Design.

Die Kommunikation zwischen dem Spiel und dem Server findet nahezu ausschließlich mittels AJaX statt; diese Technik ermöglicht es, ohne das Neuladen einer Seite einzelne Anfragen an den Server zu senden, um so Daten abzurufen oder zu speichern. Dadurch ist für das Spielen nach der Anmeldung nur ein einzelner Seitenaufruf erforderlich; die weitere Kommunikation findet dann ausschließlich über AJaX statt. Das führt auch dazu, dass die Verzögerungen innerhalb des Spieles ziemlich gering sind, da keine vollständige Seite einschließlich der Daten, die sich niemals ändern (im Beispiel von Profitopia etwa die Accountinfo-Box oder die Navigation), geladen werden muss, sondern nur ganz explizit die Daten, die relevant sind; also etwa bei dem Laden eines Nutzerprofils nur die einzelnen Daten, nicht jedoch das Layout der Seite, die diese Daten anzeigen soll (da dies bereits beim initialen Seitenaufruf geladen wurde).

Hosting
=======

Wir hosten Profitopia bei dem genialen Hoster `Uberspace`_, der neben allem für Webhosting erforderlichen noch deutlich mehr anbietet; etwa eine vollständige Linux-Shell (die insbesondere bei dem Betreiben eines Python-Projektes wie Profitopia äußerst hilfreich ist) und äußerst kompetenten Support, der innerhalb von kürzester Zeit antwortet.



.. _Django: https://www.djangoproject.com
.. _jQuery: http://jquery.com
.. _Uberspace: https://uberspace.de
