# Määrittelydokumentti

Tavoitteena on saada Drone malliltaan Parrot AR Drone pelaamaan beer pongia siten, että drone lentää vastustajan pelialueen yläpuolelle ja tiputtaa pallon mukialueelle.

## Dronen toiminta

1. Ohjelman käynnistyessä drone aloittaa lennon ja pyrkii kamerallaan löytämään kaksi mukirykelmää, joiden on tarkoitus olla ympäristössä ainoat punaiset objektit. Dronesta etäämmällä olevat mukit toimivat vastustajien mukeina.
2. Vaihtoehtoinen (jos aikaa jää): drone asettuu samaan linjaan tiimien mukien suhteen.
3. Drone aloittaa hyökkäyksen. Tiputus tapahtuu sopivassa kohtaa, apuna käytetään pohjakameran kuvaa.
4. Vaihtoehtoinen (jos aikaa jää): drone lentää takaisin oman joukkueensa heittoalueelle.

## Pallon tiputtaminen

Pallo tiputetaan laittamalla drone tekemään voltti, jolloin takaosassa oleva pallo tippuu.

## Dronen käyttö

Drone ei juuri vaadi käyttäjältä interaktiivisuutta. Koska dronen ei ole tarkoitus ymmärtää miten beer pong toimii, käytännössä ainut komento on hyökkäyksen aloittaminen. Tämä voitaisiin toteuttaa yksinkertaisimmillaan sovelluksen käynnistämisellä, tai äänikomennolla "We need air support!"

## Hyväksymiskriteerit

Projektin hyväksymiskriteeri on saada suoritettua pallon tiputus joka ainakin teoriassa voisi osua vastustajan mukiin.
