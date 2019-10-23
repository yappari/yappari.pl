---
layout: post

author: kbielen
title: Exim&#58; wysyłanie maili z systemu Linux
---

_Poniższy artykuł przedstawia instrukcję konfiguracji dla systemu Debian 6.0._

----

Konfiguracja exim'a jest wykonywana przy pomocy polecenia:

```
dpkg-reconfigure exim4-config
```

Po wywołaniu tego polecenia należy odpowiedzieć na kilka pytań, w których należy
skonfigurować serwer w trybie wysyłania maili jako `smarthost, no local mail`.

Wykorzystywane konta mailowe należy zdefiniować w pliku:

```
/etc/exim4/passwd.client
```

*Uwaga*: w przypadku korzystania z serwera poczty, do którego połączenie nie
jest szyfrowane, wymagane jest zdefiniowanie w pliku:

```
/etc/exim4/exim4.conf.localmacros
```

następującego makra:

```
AUTH_CLIENT_ALLOW_NOTLS_PASSWORDS = 1
```

Z oczywistych powodów należy unikać tego rozwiązania.
