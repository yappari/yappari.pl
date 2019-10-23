---
layout: post

author: kbielen
title: log4cxx&#58; przykłady plików konfiguracyjnych
---

Poniżej przedstawiam *przykłady konfiguracji* najbardziej przydatnych appenderów
dla biblioteki *log4cxx*:

### 1. Standardowe wyjście błędów

```
log4j.appender.myappender = org.apache.log4j.ConsoleAppender
log4j.appender.myappender.target = system.err

log4j.appender.myappender.layout = org.apache.log4j.PatternLayout
log4j.appender.myappender.layout.ConversionPattern = %d{yyyy-MM-dd HH:mm:ss} %-r [%t] %-5p: (%c) %m%n
```

### 2. Plik rotujący się przy zadanym rozmiarze</string>

```
log4j.appender.myappender = org.apache.log4j.RollingFileAppender
log4j.appender.myappender.File = ./pathtologfile/mylogfile.log
log4j.appender.myappender.maxFileSize = 100KB
log4j.appender.myappender.maxBackupIndex = 5

log4j.appender.myappender.layout = org.apache.log4j.PatternLayout
log4j.appender.myappender.layout.ConversionPattern = %d{yyyy-MM-dd HH:mm:ss} %-4r %-5p: (%c) %m%n
```

### 3. Plik rotujący się raz dziennie

```
log4j.appender.myappender = org.apache.log4j.DailyRollingFileAppender
log4j.appender.myappender.DatePattern = '.'yyyy-MM-dd
log4j.appender.myappender.File = ./pathtologfile/mylogfile.log

log4j.appender.myappender.layout = org.apache.log4j.PatternLayout
log4j.appender.myappender.layout.ConversionPattern = %d{yyyy-MM-dd HH:mm:ss} %8r [%p] [%t] %c - %m%n
```

### 4. Windows Event Log

```
log4j.appender.myappender = org.apache.log4j.nt.NTEventLogAppender
log4j.appender.myappender.Source = MyApp

log4j.appender.myappender.layout = org.apache.log4j.PatternLayout
log4j.appender.myappender.layout.ConversionPattern = %d{yyyy-MM-dd HH:mm:ss} %8r [%p] %c - %m%n
```
