---
layout: post

author: kbielen
title: Zdalne restartowanie usługi Windows z poziomu systemu Linux
---

W celu zdalnego zrestartowania usługi windows z poziomu linux'a można
wykorzystać następujące komendy:

```
net rpc service stop SERVICENAME -I IPADDRESS -U USERNAME%PASSWORD
net rpc service start SERVICENAME -I IPADDRESS -U USERNAME%PASSWORD
```

Powyższe polecenia wymagają zainstalowania pakietu _samba-common_.
