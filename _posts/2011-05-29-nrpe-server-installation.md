---
layout: post

author: kbielen
title: Jak skonfigurować serwer nrpe pod linuxem

abstract: >
    Opis konfiguracji serwera nrpe dla systemu nagios, w celu
    monitorowania miejsca na dyskach twardych na zdalnych sewerach
    z zainstalowanym systemem operacyjnym typu Linux.
---

### Instalacja oraz konfiguracja serwera nrpe

Jednym z podstawowych zadań administracyjnych jest sprawdzanie ilości wolnego
miejsca na dyskach twardych serwerów. Poniżej przedstawię w jaki sposób należy
skonfigurować system Linux, aby możliwe było monitorowanie dysków przy pomocy
systemu [Nagios](http://nagios.org/).

Jednym z możliwych rozwiązań monitorowania zasobów na zdalnych serwerach jest
instalacja [serwera
nrpe](http://exchange.nagios.org/directory/Addons/Monitoring-Agents/NRPE--2D-Nagios-Remote-Plugin-Executor/details).
Zaletami serwera nrpe jest szybkość oraz małe wykorzystanie zasobów systemu
kosztem bezpieczeństwa. Serwer nrpe nie zawiera modułu autoryzacji, a pozwala
jedynie na ograniczenie listy adresów ip, z których można nawiązać połączenie.
Alternatywą jest np. wywoływanie skryptów nagiosa poprzez ssh.

W celu skonfigurowania serwera nrpe pod systemem [Debian](http://debian.org
należy):

1. zainstalować pakiet _nagios-nrpe-server_,
2. edytować pliki znajdujące się w katalogu _/etc/nagios/nrpe_.

Lokalna konfiguracja powinna znaleźć się w katalogu _nrpe.d_ lub w pliku
_nrpe_local.cfg_. Należy zwrócić uwagę na dwie dyrektywy:

* _allowed_hosts_ - lista adresów ip, z których można nawiązać połączenie z
  serwerem nrpe,
* _command_ - w dyrektywie command znajdują się definicje poleceń, które mogą
  być zdalnie wykonane na serwerze nrpe; przykładowo dla sprawdzania wolnego
  miejsca na dysku hda1, możemy zdefiniwać następujące polecenie:

```
command[check_hda1]=/usr/lib/nagios/plugins/check_disk \
                    -w 20% -c 10% -p /dev/hda1
```

Po tych zabiegach możliwe jest już zdalne sprawdzanie ilości wolnego miejsca na
dysku (oraz innych parametrów) przy pomocy systemu Nagios. Informacje na temat
konfiguracji systemu Nagios w celu nawiązania połączenia do serwera nrpe można
znaleźć na oficjalnej stronie tego systemu.
