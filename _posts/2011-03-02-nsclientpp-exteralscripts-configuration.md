---
layout: post

author: kbielen
title: NSClient++&#58; jak skonfigurować ExternalScripts

abstract: >
    Opis konfiguracji programu NSClient++ (agent Nagios'a) w celu
    umożliwienia zdalnego wywołania dowolnego programu na serwerze
    z systemem operacyjnym Windows.
---

Poniższy opis instalacji oraz konfiguracji agenta NSClient++ dotyczy programu w
wersji 0.3.8.

### Instalacja

W celu instalacji należy skorzystać z instalatorów pobranych z [oficjalnej
strony](http://www.nsclient.org/nscp/downloads) programu.

Podczas instalacji należy zwrócić uwagę na następujące kroki:

1. ograniczenie listy adresów ip, z których można nawiązać połączenie,
2. zaznaczenie checkbox'a: "Enable NRPE server (check_nrpe)".

### Konfiguracja

Konfiguracja programu znajduje się w pliku NSC.ini (domyślna lokalizacja to:
_C:\Program Files\NSClient++\NSC.ini_).

W pliku tym należy wykonać następujące czynności:

* odkomentować moduł: CheckExternalScripts.dll,
* ustawić zmienną _script_dir_ na ścieżkę wskazującą katalog ze skryptami,
* zdefiniować odpowiednie polecenia w sekcji [External Scripts], np:

```
check_test=scripts\test.exe [arg1] [arg2]
```

Po zrestartowaniu/uruchomieniu usługi NSClient++ możemy wywołać skrypt z innej
maszyny przy użyciu narzędzia _check_nrpe_ , przykład:

```
./check_nrpe -H xxx.xxx.xxx.xxx -c check_test
```

, gdzie:

* xxx.xxx.xxx.xxx - adres IP zdalnego serwera, na którym chcemy uruchomić
  skrypt,
* check_test - nazwa zdefiniowanej komendy w sekcji [External Scripts]
  konfiguracji program NSClient++.

### Przekazywanie zdalnych parametrów do skryptu

Istnieje możliwość przekazywania parametrów do zdalnych skryptów, ale ze
względów bezpieczeństwa nie jest to zalecane.

Aby skonfigurować przekazywanie parametrów ze zdalnej maszyny należy:

* ustawić odpowiednie wartości w następujących zmiennych pliku konfiguracyjnego:
    * allow_arguments,
    * allow_nasty_meta_chars,
* zdefiniowanie komendy w następujący sposób:

```
check_test=scripts\test.exe $ARG1$ $ARG2$
```

* wywołanie polecenia _check_nrpe_ w następujący sposób:

```
./check_nrpe -H xxx.xxx.xxx.xxx -c check_test -a arg1 arg2
```
