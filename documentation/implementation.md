# Toteutusdokumentti

## Käytetyt kielet ja ympäristöt

* Ohjelmointikieli: Python2
* Dronen hallinta: PS-Drone, source: http://www.playsheep.de/drone
* Videon tulkinta ja tallentaminen: OpenCv2

## Ohjelman yleisrakenne

Ohjelma on yhdessä ajettavassa python-tiedostossa joka sisältää sekä manuaaliset kontrollit että varsinaisen autopilotin. Itsessään koodi on jaettu kolmeen osaan ja löytyy koodista seuraavassa järjestyksessä:

1. Kerran suoritettava dronen ja muuttujien alustus
2. Wait-metodi, jonka tehtävänä on antaa dronen liikkua tietyn ajan. Samaan aikaan kuitenkin halutaan seurata käyttäjän näppäinpainalluksia, joten metodi sisältää myös manuaalisen ohjauksen koodin.
3. Koodin "aivot" eli autopilotti, joka kutsuu aina tarvittaessa wait-metodia.

## Työn mahdolliset puitteet ja parannusehdotukset

* Pallon pudotus on epätarkkaa
* Pongimukin tunnistaminen on epätarkkaa
* Robotti ei saavuttanut täysin autonomista ohjausta
