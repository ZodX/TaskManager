# Task Manager rendszerspecifikáció

## 1. Mit (rendszer):
A felhasználó szemszögéből határozzuk meg az elkészítendő funkciókat a funkcionális specifikáció alapján.
* Rendszer használati esetek és lefutásai meghatározzák az oktató oldal funkcióinak meg valósulását.
* Képernyő tervek: egyedi jól megkülönböztethető megjelenési stílus,egyszerű áttekinthető elemek: háttér, keret, aktuális cetli jelzése, Dark/Light mode megvalósítása.
* Fizikai követelmények: Fizikai környezet: A weboldalnak olyan kialakítása, amely rugalmasan alkalmazkodik a különböző böngészőkhöz, annnak képernyőjének méretéhez. Ennek célja az, hogy egy optimális megjelenítést biztosítson a felhasználónak minden böngészésre alkalmas eszközön. például: desktot, moobil, laptop, tablet, egyéb eszközök. 
* Prioritás keretrendszer: A cetlik rendezése fontossági sorrend szerint, szintek megadása.
* Könnyen üzemeltethető rendszer.
* A rendszer online formában való kivitelezése.
* A rendszer távolról való elérése, az aktuális információk megjelenítéséhez
* User Interface (Felhasználói felület) megvalásítása, annak érdekében, hogy a felhasználó is interrakcióba léphessen.
* Platformfüggetlen keretrendszer

## 2. Miért (rendszer célja):

A cél az, hogy a felhasználó egy könnyen kezelhető, átlátható felület segítségével nyomon követhesse az aktív feladatait, illetve, ha szeretné, könnyedén módosíthassa, vagy csoportokra bonthassa azokat. Továbbá, az eddigi megoldott, vagy meg nem oldott feladatokat egyszerűen vissza kereshesse.

## 3. Hogyan (terv):

### 3.1. Projekt terv:

#### 3.1.1. Projekt szerepkörök, felelősségek:

* **Projekt vezető**: Az a személy, aki a projekt "tulajdonosa". Ez a személy végzi a projekt felülvizsgálatát, mind részfeladatok meghatározása, mind változtatások bekerülése terén.
* **PA** (Program Analyst): Tervezésért, fejlesztésért felelős személy. Optimális megoldások kifejlesztésére is hivatott. Programkódok írása.
* **Tesztelő**: Teszteket biztosít a projekthez, amik a kód helyes működést támasztják alá.

#### 3.1.2. Projekt munkások és felelősségeik:

* **Molnár András Imre** (GitHub: *ZodX*): *Projekt vezető, PA, Tesztelő*
* **Bacsik Mátyás** (GitHub: *bacsikmatyas*): *PA, Tesztelő*
* **Huri Patrik** (GitHub: *Hurip*): *PA*
* **Heinrich László** (GitHub: *heinrichlaszlo*): *PA*

#### 3.1.3. Ütemterv:

* **2020.09.25.**: Funkcionális működés.
* **2020.09.28.**: Tesztelés befejezése

#### 3.1.4. Mérföldkövek:

* **Új feladat létrehozása** funkció működik
* **Feladat törlése** funkció működik
* **Feladat módosítása** funkció működik
* **Feladat késznek nyilvánítása** funkció működik
* **Feladat prioritásának megadása** funkció működik
* **Feladatok csoportosítása** funkció működik
* **Feladat csoportok külön lekérdezhetősége** funkció működik
* **Oldal kinézetének módosítása(Sötét, világos, színvak mód)** funkció működik
* **Minden kívánt funkció megvalósítva**
* **Funkciók tesztlefedettsége teljes**
* **Weboldal kinézetének tesztlefedettsége teljes**

### 3.2. Funkcionális terv:
 * átláthatóság - ennek  megfelelően, egy olyan program legyen, amely minden programozó számára átlátható kódolással legyen megírva. Fontos az, hogy a programozók mindig értsék a munkatársaik logikáját. A kód legyen könnyen olvasható, hogy bárki be tudjon csatlakozni a munkába, és tudja folytatni azt.
 * javíthatóság - hibák mindig vannak, lesznek. Legyen lehetőség javítani. A javítás legyen egységes.
 * felhasználóbarát - a program felülete és kezelhetősége legyen a felhasználók életkorának megfelelő. A tervezésnél figyelembe kell venni minden lehetőséget. Erre a feladatra jelöljünk ki egy erre alkalmas kollégát, aki vezeti ezt a tevékenységet.
 * letölthető segédletek, tananyagok

### 3.3. Fizikai környezet:

A fejlesztett rendszerünk egy web applikáció lesz, tehát a frontend fejlesztéséhez a következő eszközöket fogjuk használni:

* HTML
* CSS (Bootstrap keretrendszer)

A backendhez szükséges fejlesztői eszközök:

* python3 (flask csomag)
* SQL (flask-sqlalchemy csomag)

Teszteléshez:

* Java + Selenium WebDriver + Galen keretrendszer

A kész rendszert egy Heroku nevezetű, felhő alapú PaaS-ra(Platform as a Service) helyezzük el, ami szervert biztosít számára.

### 3.4. Adatbázis terv:

A rendszerünk SQL adatbázisa egy táblát fog tartalmazni, ezáltal nem lesz kapcsolatban más táblákkal.

A tábla  oszlopai a következők:

* Id(szám): ez a generált kulcs
* feladat(szöveg): a feladat leírása
* csoport(szöveg): a feladat csoportja
* prioritás(szám): a feladat prioritása(1-10)
* utolsó módosítás(dátum): hozzáadás vagy későbbi módosítás dátuma
* kész(logikai): azt jelzi, hogy az adott feladat kész *(true)* vagy aktív *(false)*

### 3.5. Implementációs terv:

Python Flask segítségével weblap és adatbázis kontrollert készítünk.

#### 3.5.1. Üzleti logika osztályai:

* Controller.py

### 3.6. Tesztterv:

* Tesztelni kell az oldal összes funkcióját, ezzel biztosítva a helyes működést.
* Tesztelni kell az oldal megjelenését, hogy minden láthatóan és olvashatóan jelenik-e meg a felhasználó számára.

### 3.7. Telepítési terv:

A rendszer használatához a gépeken egyedül egy bönésző telepítésére van szükség, mivel a Task Managert egy Heroku nevezetű paltformra helyezzük el. Ez egy felhő alapú szolgáltatás, amin szerverünket működtethetjük.

## 4. Mikor:

* Legkésőbb az osztályozásig véglegesíteni kell a rendszert.

## 5. Miből (erőforrások):
