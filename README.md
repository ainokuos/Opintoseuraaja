# **OT-Harjoitustyö**
## Opintoseuraaja
Sovelluksen avulla käyttäjällä on mahdollista pitää kirjaa omista opinto suorituksistaan sekä opintomenestyksestä. 
### Viimeisin versio
[Opintoseuraaja](https://github.com/ainokuos/ot-harjoitustyo/releases/tag/Opintoseuraaja)

Edeltävät:

[Viikko6](https://github.com/ainokuos/ot-harjoitustyo/releases/tag/viikko6)

[Viikko5](https://github.com/ainokuos/ot-harjoitustyo/releases/tag/viikko5)

## Dokumentaatio

[Käyttöohje](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Käyttöohje.md)

[Vaatimusmäärittely](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Vaatimusmäärittely.md)

[Työaikakirjanpito](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Työaikakirjanpito.md)

[Arkkitehtuuri](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Arkkitehtuuri.md)
 
 [Testaus](https://github.com/ainokuos/ot-harjoitustyo/blob/master/dokumentaatio/Testaus.md)


## Asennus

1. Asenna riippuvuudet komennolla:
```
poetry install
```

2. Alusta sovellus komennolla:
```
poetry run invoke build
```

3.Käynnistä sovellus komennolla:
```
poetry run invoke start
```
## Komentorivi

Testaukset voi suorittaa komennolla:
```
poetry run invoke test
```
Testikattavuuden voi tarkistaa komennolla:
```
poetry run invoke coverage
```
Testikattavuusraportin saa komennolla:
```
poetry run invoke coverage-report
```
Laatutarkistuksen voi suorittaa komennolla:
```
poetry run invoke lint
```
