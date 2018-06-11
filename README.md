# Muistilista
[Muistilista verkkosivu](https://tsoha-muistilista-kesa.herokuapp.com)  &larr; muistilista on käytettävissä tästä linkistä

(Verkkosivu ei toiminut, mutta saattaa olla, että heroku ei ollut viellä päivittynyt. Kaikki toimi kuitenkin paikallisesti, ja heroku yhteys toimi ennenkin.)

Testausta varten:

Käyttäjä: Tsoha

Salasana: salasana

Älä poista testauksessa seuraavia askareita: "tsoha", "unelma"

Älä poista testauksessa seuraavia luokkia: "harkkis", "työ"

Ne ovat esittämässä yhteenvetokyselyä. Voi luoda uusia askareita/luokkia, mitä voi sitten poistella.

## Dokumentaatio

[Aihekuvaus](https://github.com/Savolainen95/Tsoha-Muistilista/blob/master/dokumentaatio/Aihekuvaus.md)

[Käyttötapaukset](https://github.com/Savolainen95/Tsoha-Muistilista/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6tapaukset.md)

[Alustava Luokkakaavio](https://github.com/Savolainen95/Tsoha-Muistilista/blob/master/dokumentaatio/kuvat/Tsoha%20luokkakaavio.png)

#### vaativampi yhteenvetokysely ####

string = ()

        stmt = text('SELECT luokka.nimi FROM task, luokka, taskluokka'
        ' WHERE taskluokka.task_id = ' + str(apuid) +
        ' AND taskluokka.luokka_id = luokka.id'
        ' AND taskluokka.task_id = task.id') 
        
Yllä mainittu kysely palauttaa sivulle tasks/specs/<task.id>/ listan askareeseen liitetyistä luokista. Luokkia ei pysty viellä kuitenkaan selaimen kautta liittämään askareisiin, koska en keksinyt siihen ratkaisua. Käyttäjällä "Tsoha" pitäisi olla kuitenkin askare "tsoha", jolla on luokat "harkkis" ja "työ". Askareella "unelma" on vain luokka työ. (älä testatessasi siis mieluusti poista näitä luokkia ja askareita, että yhteys säilyy).

