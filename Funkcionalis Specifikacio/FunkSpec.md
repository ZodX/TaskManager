# Task Manager funkcionális specifikáció

## 1. A rendszer céljai és nem céljai

### 1.1 A rendszer céljai

Az elkészített rendszerrel a felhasználó képes lesz:

* feladatait egy helyen, átláthatóan nyomonkövetni, felesleges szemét *(cetlik)* generálása nélkül
* új feladatokat hozzáadni, módosítani a már létrehozottakat
* csoportosítani a feladatokat
* megadni a feladatok fontosságát *(prioritás)*
* törölni, ha esetleg rosszul adott meg valamit, vagy késznek nyilvánítani a feladatokat
* feladatok listázása *(összes vagy egy adott csoport)*
* az elkészített feladatok listájának lekérdezésére
* megváltoztatni az oldal témáját *(dark/light/colorblind)*
* a fentebb felsoroltakat akármilyen internethasználatra alkalmas eszközön végrehajtani

### 1.2 A rendszer ***NEM*** céljai

Az elkészített rendszerrel a felhasználó ***NEM*** lesz képes:

* több felhasználó adatait külön-külön kezelni
* megtekinteni, hogy milyen akciókat hajtott végre az oldalon belül *(log)*
* széleskörűen testreszabni a rendszert *(értsd: csak light/dark/colorblind téma)*
* egyszerre több csoportba is elhelyezni egy feladatot
* a hozzáadott feladatokat rendezni *('érkezési sorrend')*

## 2. Jelenlegi helyzet

* Jelenleg rengeteg a felhamozódó feladat számomra, ezeket nyomon követni egyre nehezebb, átláthatatlan az egész számomra.
* Pillanatnyilag, a helyzet az, hogy külön csoportkra bontom a feladataimat, és ezeket egy cetlire írom, ami nem a 
* legkényelmesebb megoldás.
* Ez a helyzet, nem a legoptimálisabb, mivel az átrendezése időigényes, sok problémával jár, illetve a matricák
* veszítenek a   tapadósságból, ezzel sok szemetet generálunk, valamint több lesz a költségünk is. 

## 3. Vágyálom rendszer

* A célunk egy könnyen átlátható, és kezelhető weboldal, ezzel a mindennapi folyamatokat szeretnénk leegyszerűsíteni.
* A terv egy egyszerűen szerkeszthető weboldal. Szeretnénk továbbá azt is elérni, hogy a weboldal online is kezelhető legyen,
* ezzel  elérni azt, hogy  távolról is elérhetőek legyenek az aktuális információk. Nem elfogadható csak Microsoft Windows operációs
* rendszeren üzemeltethető rendszerre vonatkozó javaslat. A weboldallal azt szeretnénk elérni, hogy könnyen üzelemtethető legyen, és
* elvárt a platformfüggetlenség is.
* Az online megjelenésnél fontos az, hogy lehetőleg az össze erre alkalmas eszközön elérhető legyen (mobil telefon, tablet), 
* reszponzív felülettel (rugalmasan alkalmazkodik a különböző böngészőkhöz).

## 4. Jelenlegi üzleti folyamatok

* Új feladat hozzáadása (Cetlire írás -> cetli letépése -> cetli táblára ragasztása)
* Feladat törlése (Cetli levétele a tábláról -> cetli kukába dobása)
* Feladatok csoportosítása (Cetlik egy adott helyre csoportosítása a táblán)
* Feladat késznek nyilvánítása (Cetli ‘kész’ csoportba helyezése)
* Feladat frissítése/módosítása (Új cetli írása(új feladat))

## 5. Igényelt üzleti folyamatok

* Feladat módosítása (Modify/Update task)
* Felhasználóbarát UI (Dark/Light mode + Színvak mode)
* Feladatok prioritásának megadása (Prioritizing tasks)

## 6. Követelménylista

* Könnyen üzemeltethető rendszer.
* Reszponzív design. A célja, hogy a weboldalunk rugalmasan alkalmazkodjon a különböző böngészők képernyőjének méretéhez, 
* így eléri azt, hogy egy optimális megjelenést biztosítson a felhasználónak minden eszközön amely képes böngészésre.

## 7. Használati esetek

### 7.1 Aktorok meghatározása

Esetünkben az egyetlen aktorként a ***felhasználót*** sorolnám fel, mivel rendszerünkkel más nem tud interakcióba lépni.

### 7.2 Használati eset diagram

![Task Manager használati eset diagram](src/Use_Case_Diagram_for_TaskManager.png)

## 8. Megfeleltetés

* Új feladat hozzáadása - **Kidolgozva**
* Feladat törlése - **Kidolgozva**
* Feladatok csoportosítása - **Kidolgozva**
* Feladat késznek nyilvánítása - **Kidolgozva**
* Feladat módosítása - **Kidolgozva**
* Felhasználóbarát UI (Dark/Light mode + Színvak mode) - **Kidolgozva**
* Feladatok prioritásának megadása - **Kidolgozva**

## 9. Képernyőtervek

* Legyen teljes , a felhasználó a felhasználói felületen keresztül a program minden funkciója elérhető legyen.
* A felhasználói felület legyen szellős és átlátható, jól különüljenek el egymástól az egyes funkciók, funkció csoportok.
* A felületnek olyan kifejezéseket kell használnia, amelyek megfelelnek a rendszert legtöbbet használók tapasztalatainak.
* A felületnek konzisztensnek kell lennie, azaz lehetőség szerint hasonló műveleteket hasonló módon kell realizálnia.
* Legyen visszaállíható , a felületnek rendelkeznie kell olyan mechanizmusokkal , amelyek lehetővé teszik a felhasználók számára a hiba után történő visszaállítást.
* A felületnek megfelelő interakciós lehetőségekkel kell rendelkeznie a
rendszer különféle felhasználói számára.

  ![kezdokepernyo](src/kezdokepernyo.jpg)
  ![kepernyo](src/kepernyo.jpg)

## 10. Forgatókönyvek

Elfelejtő Jenő a mindennapok során egyre több és több feladattal találja szembe magát és ez nagyon megerölteti pici agyát. Nem tudja , hogy mikor mit és hol kellene csinálnia , így gyakran csak a napot lopja. Próbálta már a teendőit kezére , cetlikre felírni. De a sok-sok cetlit nem bírta magával cipelni. Kétségbe esvén , nem tudván mit tegyen barátja Bará Tamás mutatott neki egy honlapot , ahol csupán internetre lesz szüksége és akár telefonról , táblagépről , számítógépről a napi teendőit bármikor elérheti. Teendőivel ha kész van nyugodtan törölheti és az összes kis "cetlit" a zsebében cipelheti. Ezután Elfelejtő Jenő fejéből teendő el nem vész és minden munkájával időben kész.

## 11. Fogalomszótár

* **Reszponzív design** - A reszponzív design a weboldalnak egy olyan kialakítása, amelyik rugalmasan alkalmazkodik a különböző böngészők képernyőjének méretéhez annak érdekében, hogy optimális megjelenést biztosítson a felhasználónak minden böngészésre alkalmas eszközön, legyen az desktop, laptop, mobil, vagy tablet.
* **UI** - User Interface (Felhasználói felület). A felület, amivel a felhasználó interrakcióba lép.
* **Konzisztens** - Következetes
