---
layout: post

author: kbielen
title: Visual Studio&#58; zmienne środowiskowe

abstract: >
    Propozycja używania zmiennych środowiskowych w plikach
    projektów Visual Studio w celu separacji lokalnej konfiguracji
    komputerów programistów od konfiguracji projektu.
---

### Przykład

W przypadku używania bibliotek Boost możemy stworzyć dwie zmienne środowiskowe:

| Zmienna środowiskowa | Wartość |
| -------------------- | ------- |
| YprBoost_1.42 | C:\Program Files\boost\boost_1_42 |
| YprBoost_1.43 | C:\Program Files\boost\boost_1_43 |

, a następnie odwoływać się do nich w sekcjach projektu VS przy pomocy
następującej składni: `$(YprBoost_1.42)`.

### Zalety

Dzięki powyższemu podejściu możemy:

* "przypiąć" projekt do odpowiedniej wersji biblioteki,
* pozwolić programistom na instalowanie bibliotek na własnych maszynach w
  preferowanym przez nich miejscu.

Powyższe podejście możemy także wykorzystać do używania zewnętrznych narzędzi
(np. Inno Setup, 7-zip) we wszelakich skryptach.

### Konfiguracja zmiennych środowiskowych z linii poleceń

W celu zarządzania zmiennymi środowiskowymi w systemie windows z linii
poleceń można użyć narzędzia *setx*:

* [manual](http://msdn.microsoft.com/en-us/library/cc755104%28WS.10%29.aspx)
* [download dla win xp](http://www.microsoft.com/downloads/en/details.aspx?FamilyID=49ae8576-9bb9-4126-9761-ba8011fabf38&displaylang=en)
