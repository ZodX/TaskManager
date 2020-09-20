# Task Manager rendszerspecifikáció

## 1. Mit (rendszer):

## 2. Miért (rendszer célja):

## 3. Hogyan (terv):

### 3.1. Projekt terv:

### 3.2. Funkcionális terv:

### 3.3. Fizikai környezet:

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

### 3.6. Tesztterv:

### 3.7. Telepítési terv:

A rendszer használatához a gépeken egyedül egy bönésző telepítésére van szükség, mivel a Task Managert egy Heroku nevezetű paltformra helyezzük el. Ez egy felhő alapú szolgáltatás, amin szerverünket működtethetjük.

## 4. Mikor:

* Legkésőbb az osztályozásig véglegesíteni kell a rendszert.

## 5. Miből (erőforrások):
