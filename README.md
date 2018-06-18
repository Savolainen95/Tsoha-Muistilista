# Muistilista
[Muistilista verkkosivu](https://tsoha-muistilista-kesa.herokuapp.com)  &larr; muistilista on käytettävissä tästä linkistä

Testausta varten:

Käyttäjä: Tsoha

Salasana: Salasana

Uuden käyttäjän voi luoda, mutta hänellä ei valmiina askareita, eikä askareiden yhteyksien luomista luokkiin ole saatu viellä toimimaan.
Luokat ovat kuitenkin kaikille samat.

Viikko 5: Sain lisättyä askareiden lisäys ikkunaan checkit kaikille mahdolisille luokille, mutta formin kanssa lisäys toi haasteita. Ohjauksessa tähän ei löytynyt apua, niin yritän selvittää asiaa. En liittänyt autorisointia osaksi muistilistaani, sillä se ei tuo suuniteltuun ohjelmaani mitään, ja se aiheutti muualla koodissa ongelmia. Kaikki askareet ovat kuitenkin hekilökohtaisia, eivätkä ne ole muille käyttäjille näkyvissä.

Paranneltu myös toiminnallisuutta siellä täällä, ja yritetty saada sivua hieman kauniimman näköistä.



## Dokumentaatio

[Aihekuvaus](https://github.com/Savolainen95/Tsoha-Muistilista/blob/master/dokumentaatio/Aihekuvaus.md)

[Käyttötapaukset](https://github.com/Savolainen95/Tsoha-Muistilista/blob/master/dokumentaatio/k%C3%A4ytt%C3%B6tapaukset.md)

[Alustava Luokkakaavio](https://github.com/Savolainen95/Tsoha-Muistilista/blob/master/dokumentaatio/kuvat/Tsoha%20luokkakaavio.png)

#### vaativampi yhteenvetokysely ####

def askareen_luokat(apuid):

        string = ()
        stmt = text('SELECT luokka.nimi FROM task, luokka, taskluokka'
        ' WHERE taskluokka.task_id = ' + str(apuid) +
        ' AND taskluokka.luokka_id = luokka.id'
        ' AND taskluokka.task_id = task.id')

        res = db.engine.execute(stmt)
        luokat = []
        for row in res:
            luokat.append(row[0])
        return luokat
        

def luokan_askareet(apuid):

        stmt = text('SELECT task.name FROM taskluokka, task, luokka'
        ' WHERE taskluokka.luokka_id = ' + str(apuid) +
        ' AND taskluokka.luokka_id = luokka.id'
        ' AND taskluokka.task_id = task.id')

        res = db.engine.execute(stmt)
        askareet = []
        for row in res:
            askareet.append(row[0])
        return askareet
        
Ylempänä mainittu kysely palauttaa sivulle tasks/specs/<task.id>/ listan askareeseen liitetyistä luokista. 
Sama on tehty myös toisten päin, eli alempi kysely palauttaa sivulle luokka/specs/<luokka.is> luokille kaikki siihen liitetyt askareet.



