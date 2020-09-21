# Task Manager rendszerspecifikáció

## 1. Mit (rendszer):

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

### 3.3. Fizikai környezet:

### 3.4. Adatbázis terv:

### 3.5. Implementációs terv:

Python Flask segítségével weblap és adatbázis kontrollert készítünk.

#### 3.5.1. Üzleti logika osztályai:

* Controller.py

### 3.6. Tesztterv:

* Tesztelni kell az oldal összes funkcióját, ezzel biztosítva a helyes működést.
* Tesztelni kell az oldal megjelenését, hogy minden láthatóan és olvashatóan jelenik-e meg a felhasználó számára.

### 3.7. Telepítési terv:

## 4. Mikor:
* Legkésőbb az osztályozásig véglegesíteni kell a rendszert.

## 5. Miből (erőforrások):
