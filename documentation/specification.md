# Määrittelydokumentti

Tavoitteena on saada Drone malliltaan Parrot AR Drone pelaamaan beer pongia siten, että drone lentää vastustajan pelialueen yläpuolelle ja tiputtaa pallon mukialueelle.

## Dronen toiminta

1. Ohjelman käynnistyessä drone aloittaa lennon ja pyrkii kamerallaan löytämään kaksi mukirykelmää, joiden on tarkoitus olla ympäristössä ainoat punaiset objektit. Dronesta etäämmällä olevat mukit toimivat vastustajien mukeina.
2. Vaihtoehtoinen (jos aikaa jää): drone asettuu samaan linjaan tiimien mukien suhteen.
3. Drone aloittaa hyökkäyksen. Koska kamera voi katsoa vain eteenpäin eikä sitä voi kallistaa, tiputus tapahtuu tietyn ajan kuluessa siitä kun mukit katoavat dronen kameran näkökentästä. Kyseinen aika selvitetään manuaalisella hienosäädöllä.
4. Vaihtoehtoinen (jos aikaa jää): drone lentää takaisin oman joukkueensa heittoalueelle.

## Pallon tiputtaminen

Dronessa on USB-liitin, mutta vaikuttaa siltä että datalinkkiä tai ylipäätään mitään kontrollia ei ole mahdollista muodostaa mahdollisiin oheislaitteisiin. Mikäli tämä kuitenkin on mahdollista, eräs mahdollisuus olisi kiinnittää USB-liittimeen sähkömagneetti joka pitelee palloa kiinni dronen takaosassa. Helpoin toteutus lienee liimata palloon jotain magneettista.

Koska on odotettavissa ettei USB-ratkaisu ole mahdollinen, varatoteutus on taiteilla rautalangasta pallonpidike josta pallo irtoaa tarpeeksi suuren jarrutuksen aiheuttaman kallistuksen yhteydessä.

Jos kumpikaan ylläolevista ei toimi, projekti uudelleennimetään RaivoDroneksi ja dronen uusi tarkoitus on lentää vastustajan mukeja päin. Testaus tehdään tyhjillä mukeilla.

## Dronen käyttö

Drone ei juuri vaadi käyttäjältä interaktiivisuutta. Koska dronen ei ole tarkoitus ymmärtää miten beer pong toimii, käytännössä ainut komento on hyökkäyksen aloittaminen. Tämä voitaisiin toteuttaa yksinkertaisimmillaan sovelluksen käynnistämisellä, tai äänikomennolla "We need air support!"

## Hyväksymiskriteerit

Projektin hyväksymiskriteeri on saada suoritettua pallon tiputus joka ainakin teoriassa voisi osua vastustajan mukiin.
