---
layout: post

author: kbielen
title: Monitorowanie systemów z użyciem Collectd oraz Graphite

abstract_only_header: >
    Czyli jak na bieżąco zbierać statystyki wykonania
    z naszych aplikacji (np. liczbę zalogowanych użytkowników) oraz
    jak wizualizować te dane na grafach w interfejsie www.
---

W celu zbierania statystyk z naszych systemów i aplikacji takich jak np.
obciążenie procesora, zużycie pamięci, możemy użyć pary narzędzi
[collectd](https://collectd.org/) oraz
[graphite](https://graphite.readthedocs.org/en/latest/).

Aplikacja _collectd_ odpowiada za zbieranie oraz przesyłanie statystyk z
serwerów i aplikacji, nastomiast aplikacja _graphite_ przechowuje zebrane
statystyki oraz zapewnia interfejs www do rysowania grafów oraz ich
przeglądania.

Zaletami tego systemu są m.in.:
* zbieranie statystyk z maksymalnie *1-dno sekundowym interwałem*,
* wygodny i czytelny interfejs www z funkcją _auto-refresh_,
* prosta *możwliość rozbudowy systemu* o zbieranie *specyficznych statystyk* z
  naszych aplikacji (z użyciem np. pluginu
  [exec](https://collectd.org/wiki/index.php/Plugin:Exec) w aplikacji
  _collectd_).

W celu skonfigurowania tego typu monitorowania można zapoznać się z następującym
tutorialem, w którym w przystępny sposób wyjaśniono ten temat:
* [How To Install and Use Graphite on an Ubuntu 14.04
  Server](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-graphite-on-an-ubuntu-14-04-server)
* [How To Configure Collectd to Gather System Metrics for Graphite on Ubuntu
  14.04](https://www.digitalocean.com/community/tutorials/how-to-configure-collectd-to-gather-system-metrics-for-graphite-on-ubuntu-14-04)
