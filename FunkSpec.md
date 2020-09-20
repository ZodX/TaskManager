# Task Manager funkcionális specifikáció

## 1. A rendszer céljai és nem céljai

### 1.1 A rendszer céljai

Az elkészített rendszerrel a felhasználó képes lesz:

* feladatait egy helyen, átláthatóan nyomonkövetni, felesleges szemét *(cetlik)* generálása nélkül
* új feladatokat hozzáadni, módosítani a már létrehozottakat
* csoportosítani a feladatokat
* megadni a feladatok fontosságát *(prioritás)*
* törölni, ha esetleg rosszul adott meg valamit, vagy késznek nyilvánítani a feladatokat
* az elkészített feladatok listájának lekérdezésére
* megváltoztatni az oldal témáját *(dark/light/colorblind)*
* a fentebb felsoroltakat akármilyen internethasználatra alkalmas eszközön végrehajtani

### 1.2 A rendszer ***NEM*** céljai

Az elkészített rendszerrel a felhassználó ***NEM*** lesz képes:

* több felhasználó adatait külön-külön kezelni
* megtekinteni, hogy milyen akciókat hajtott végre az oldalon belül *(log)*
* széleskörűen testreszabni a rendszert *(értsd: csak light/dark/colorblind téma)*
* egyszerre több csoportba is elhelyezni egy feladatot
* a hozzáadott feladatokat rendezni *('érkezési sorrend')*

## 2. Jelenlegi helyzet
Egyre több a felhalmozódó feladat, amiket egyre nehezebb nyomon követni.
Jelenleg egy táblán külön csoportokra bontva, azon belül cetlikre íródnak a feladatok.
Ez a módszer nem a legoptimálisabb, macerás átrendezni stb... (A matricák veszítenek a tapadósságból ==> sok szemét  + költség)

## 3. Vágyálom rendszer
Egy könnyen átlátható és kezelhető weboldal, ahol könnyen megvalósíthatóak a folyamatok. 
Egyszerű szerkeszthetőség. Szeretném weboldalunk online kezelését is megoldani, hogy  távolról is láthassam az aktuális információkat.
Nem elfogadható csak Microsoft Windows operációs rendszeren üzemeltethető rendszerre vonatkozó javaslat.
A weboldal könnyen üzemeltethető legyen. Elvárt a platformfüggetlenség.
Az online megjelenés lehetőleg mobil telefonon, tableten is működjön, reszponzív felülettel.

## 4. Jelenlegi üzleti folyamatok
* Új feladat hozzáadása (Cetlire írás -> cetli letépése -> cetli táblára ragasztása)
* Feladat törlése (Cetli levétele a tábláról -> cetli kukába dobása)
* Feladatok csoportosítása (Cetlik egy adott helyre csoportosítása a táblán)
* Feladat késznek nyilvánítása (Cetli ‘kész’ csoportba helyezése)
* Feladat frissítése/módosítása (Új cetli írása(új feladat))

## 5. Igényelt üzleti folyamatok
* Feladat módosítása (Modify/Update task)
* Feladat határidő megadása (Deadline)
* Felhasználóbarát UI (Dark/Light mode + Színvak mode)
* Feladatok prioritásának megadása (Prioritizing tasks)

## 6. Követelménylista
* Könnyen üzemeltethető rendszer
* Reszponzív design

## 7. Használati esetek

## 8. Megfeleltetés

## 9. Képernyőtervek

## 10. Forgatókönyvek
