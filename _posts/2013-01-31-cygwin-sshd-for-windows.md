---
layout: post

author: kbielen
title: Cygwin&#58; sshd pod windows
---

Często w pracy administracyjnej/utrzymaniowej napotykamy się na problem
związanym z zarządzaniem zdalnymi serwerami z zainstalowanym systemem typu
windows. Wielu z nas jest przyzwyczajonych do standardu zwanego _ssh_, a nauka
windowsowych protokołów zdalnego zarządzania wydaje się zbędnym wysiłkiem.

Pośród kilku rozwiązań serwerów ssh, które pojawiły się na "rynku" jedynym z
testowanych, które spełniło moje potrzeby jest zainstalowanie
[Cygwin'a](http://www.cygwin.com/).

Z serwerem _ssh_ wchodzącym w skład pakietu cygwin bez problemu działają m.in .:

* pary kluczy publiczny/prywatny typu _rsa_ oraz _dsa_,
* narzędzie [fabric](http://fabfile.org),

dzięki czemu osiągamy dość dobrą iluzję pracy ze zwykłym serwerem typu Linux.

W rozważaniach pominiemy temat, czy jest to rozwiązanie nadające się dla
produkcyjnych instalacji naszych serwerów, ale na pewno pozwoli ono na
wygodniejszą pracę na maszynach testowych oraz developerskich.

### Instalacja

W celu zainstalowania serwera należy:

1. pobrać i zainstalować [cygwin'a](http://cygwin.com/setup.exe),
2. podczas instalacji należy zwrócić uwagę na zainstalowanie pakietu `openssh`,
3. uruchomić skryt `cygwin.bat`, który znajduje się w lokalizacji, do której
   zainstalowaliśmy program cygwin,
4. z poziomu powłoki cygiwna uruchomić skrypt: `ssh-host-config`, a następnie
   odpowiedzieć na klika pytań, a uwagę należy zwrócić m.in. na pytanie: _Do you
   want to install sshd as a service?_ *yes*.
5. uruchomić _service_ sshd np. z poziomu panelu "services.msc".

### Konfiguracja dostępu użytkowników

Po zainstalowaniu serwera ssh należy skonfigurować dostępy dla użytkowników,
którzy powinni mieć możliwość logowania się do serwera ssh. W celu dodania
możliwości logowania się _lokalnego_ użytkownika do serwera ssh, należy wywołać
następujące polecenie w konsoli _cygwin'a_:

```
mkpasswd -l -u nazwa_użytkownika >> /etc/passwd
```

### W sieci:

Bardziej dokładny opis instalacji cygwin'a oraz sshd można znaleźć np. pod
adresem:
* [oracle.com: Installing Cygwin and Starting SSH
  Daemon](http://docs.oracle.com/cd/E24628_01/install.121/e22624/preinstall_req_cygwin_ssh.htm)
