.. _employees:

Personal
########

Jede Firma benötigt Personal, um handlungsfähig zu sein. Dieses verwaltet die einzelnen Gebäude und deren Produktionen. Jeder Mitarbeiter hat nur begrenzte Kapazitäten und kann sich daher nur um eine bestimmte Anzahl an Gebäuden kümmern. Konkret kann jeder Mitarbeiter bis zu 100 Gebäudelevel verwalten. Dabei ist es egal, ob ein einzelnes Gebäude diese 100 Level aufbraucht, oder ob diese über mehrere verschiedene Gebäude verteilt sind.

Fähigkeitslevel
===============

Jeder Mitarbeiter hat ein Fähigkeitslevel. Dieses liegt zunächst bei 1 und wird durch jede Personalfortbildung erhöht. Dabei kann dieses Level maximal dem dreifachen des Spielerlevels entsprechen.

Effizenz
========

Abhängig von dem Fähigkeitslevel und der Motivation arbeitet der Mitarbeiter mit einer unterschiedlichen Effizienz. In Level 1 beträgt diese 15% und steigt jeweils mit dem Faktor 1,1 an (sie berechnet sich also durch die Funktion :math:`f(x) = 13,9 + 1,1x`). Durch dieses lineare Wachstum ist der durch eine Fortbildung erzielte Vorteil in jedem Level identisch, eine Fortbildung von Level 299 auf Level 300 bringt also einen ebensogroßen Vorteil wie eine Fortbildung von Level 1 auf Level 2; nur die Kosten der beiden Fortbildungen sind unterschiedlich.

Die maximale Effizienz eines Mitarbeiters im Fähigkeitslevel 300 liegt also bei 343,9%.

Motivation
==========

Jeder Mitarbeiter hat eine Motivation, die angibt, wie sehr dieser sich für seinen Job einsetzt. Zunächst liegt diese Motivation bei 100%, sinkt allerdings alle 7 Tage um einen zufälligen Wert zwischen 0,01 und 0,5 Prozent. Um die Motivation wiederherstellen zu können, ist eine Gehaltserhöhung erforderlich.
Die Motivation wirkt sich unmittelbar auf die Effizienz des Mitarbeiters aus. Das heißt, dass ein Mitarbeiter mit einer Motivation von 50% nur mit der Hälfte seiner eigentlichen Effizienz arbeitet.

Gehalt
======

Jeder Mitarbeiter erhält ein bestimmtes Gehalt, das täglich gegen 2 Uhr ausgezahlt wird. Dieses beträgt zunächst 5 € und steigt während des Spielverlaufs dadurch an, dass Du den Mitarbeitern Gehaltserhöhungen anbieten musst, damit sich ihre Motivation nicht zu sehr verringert.

Sollte Dein Konto nicht ausreichend gedeckt sein, um dieses Gehalt zahlen zu können, sinkt die Motivation der Mitarbeiter und sie arbeiten mit einer geringeren Effizienz. Hierüber erhältst Du bei jedem fehlgeschlagenen Bezahlungsversuch eine Benachrichtigung per Ingame-Nachricht.

Gehaltserhöhung
---------------

Um die Motivation eines Mitarbeiters zu erhöhen, ist eine Gehaltserhöhung erforderlich. Dabei wird die Motivation jeweils um denselben Anteil gesteigert wie das Gehalt. Wenn du zum Beispiel einen Mitarbeiter eingestellt hast, der mit einer Motivation von 70% arbeitet und ein Gehalt von 10 € erhält, so würde eine Gehaltserhöhung auf 15 € (also eine Erhöhung des Gehalts um 50%) zu einer Motivation von 95% (:math:`70\% + 50\% \cdot 70\%`) führen.

Dadurch bietet es sich an, Mitarbeitern möglichs oft eine Gehaltserhöhung anzubieten, da die erforderliche Höhe zum Erreichen einer Motivation von 100% exponentiell steigt, je weiter die Motivation sich von 100% entfernt. Im Idealfall bietest Du den Mitarbeitern also immer unmittelbar nach dem Verlust der maximalen Motivation (also jede Woche) eine neue Gehaltserhöhung an.

.. _employees_training:

Personalfortbildung
===================

Um die Effizenz der Mitarbeiter zu steigern, gibt es die Möglichkeit der Fortbildung. Während der Fortbildung beträgt die Effizienz des Mitarbeiters nur einen Viertel der regulären Effizienz (also etwa statt 20% nur 5%).

Kosten
------

Die Kosten für die Fortbildung steigen mit dem Level des Mitarbeiters. Die erste Fortbildung (auf Level 2) kostet 20 €, jede weitere ist um 4% teurer. Damit kostet etwa die höchste Fortbildung auf Level 300 knapp 2,5 Millionen Euro.

Dauer
-----

Jede Mitarbeiterfortbildung dauert – unabhängig von dem Level – 24 Stunden.

Limitierung
-----------

Mitarbeiter können maximal bis zu dem dreifachen des Spielerlevels fortgebildet werden. Hat ein Spieler etwa das Level 5, so beträgt das höchste Level, das ein Mitarbeiter dieses Spielers haben kann, 15.

Entlassung
==========

Ein Mitarbeiter kann frühestens 7 Tage nach seiner Einstellung entlassen werden. Die Entlassung ist nur dann möglich, wenn auch ohne diesen Mitarbeiter ausreichend viele Mitarbeiter des entsprechenden Typs vorhanden sind, um alle Gebäude weiterhin betreiben zu können.

Mitarbeitertypen
================

Es gibt für jeden Gebäudetyp einen Mitarbeitertyp sowie den Sekretär. Derzeit existieren in Profitopia die folgenden Mitarbeiter.

 * Sekretär
 * Brunnenschöpfer
 * Minenarbeiter
 * Grundstofffabrikarbeiter
 * Mikroelektroniker
 * Computerbauer

Sekretär
--------

Der Sekretär ist ein besonderer Mitarbeitertyp; er wird benötigt, um sämtliche Personal- und Bauaktionen zu verwalten. Daher ist es nicht möglich, andere Mitarbeiter einzustellen, solange noch kein Sekretär vorhanden ist; dieser sollte also als erstes angestellt werden. Gleichzeitig kann jede Firma nur einen einzigen Sekretär beschäftigen.


Beschränkungen
==============

Mit dem Sekretär ist die Einstellung von bis zu 10 Mitarbeitern möglich. Zusätzlich ermöglicht jede zweite Fortbildung des Sekretärs einen weiteren Mitarbeiter.

Damit können insgesamt 160 Mitarbeiter – einschließlich des Sekretärs – eingestellt werden.
