---
layout: post

author: kbielen
title: Boost&#58; snippety

abstract: >
   Przykłady kodu wykorzystującego biblioteki boost do&#58; serializacji
   obiektów, rekursywnego iterowania po katalogach oraz
   używania wyrażeń regularnych. Przedstawione przykłady
   zostały zaimplementowane dla bibliotek boost w wersji 1.45.
---

### Serializacja obiektów

Poniżej znajduje się przykład wykorzystania biblioteki boost do serializacji
struktur danych do buforów znaków.

Należy zainkludować następujące pliki:

{% highlight cpp linenos %}
#include <boost/archive/binary_iarchive.hpp>
#include <boost/archive/binary_oarchive.hpp>
#include <boost/serialization/vector.hpp>
{% endhighlight %}

W celu serializacji struktury/klasy należy stworzyć definicję klasy w
następujący sposób:

{% highlight cpp linenos %}
struct MyStruct
{
   int x;
   std::string str;
   std::vector<int> vec;

private:

   friend class boost::serialization::access;

   template<class Archive>
   void serialize(Archive &ar, const unsigned int version)
   {
      ar & x;
      ar & str;
      ar & vec;
   }
}
{% endhighlight %}

W celu serializacji do buffora należy napisać następujący kod:

{% highlight cpp linenos %}
try
{
   std::stringbuf sb;
   boost::archive::binary_oarchive oa(sb);
   oa & data;

   int data_size = sb.str().length();
   std::string str = sb.str();
   const char *buff = str.c_str()

   // TODO: ...dalsze operacje
}
catch (std::exception &e)
{
   // TODO: obsługa wyjątku
}
{% endhighlight %}

W celu deserializacji należy napisać następujący kod:

{% highlight cpp linenos %}
try
{
   // TODO: ...tutaj tworzymy/odbieramy bufor danych 'buff'
   // o rozmiarze 'buff_size'
   //
   // Uwaga!!! należy zwrócić uwagę na użycie obiektu tymczasowego
   // typu 'std::string'

   std::stringbuf sb(std::string(buff, buff_size));
   boost::archive::binary_iarchive ia(sb);
   ia & data;

   // TODO: ...dalsze operacje na strukturze danych 'data'
}
catch (std::exception &e)
{
   // TODO: obsługa wyjątku
}
{% endhighlight %}

### Rekursywne iterowanie po katalogu

Biblioteka Boost::Filesystem implementuje przydatne funkcje służące do
manipulacji ścieżkami, plikami oraz katalogami systemu plików. Poniżej znajduje
się przykład prezentujący rekursywne iterowanie po katalogu.

{% highlight cpp linenos %}
#include <boost/filesystem.hpp>

namespace bf = boost::filesystem;

int main()
{
   bf::path path("test_path");

   if (bf::exists(path) && bf::is_directory(path))
   {
      /*
       * Iteratory domyślnie wskazują koniec kolekcji
       */
      bf::recursive_directory_iterator iter(path), end;
      for ( ; iter != end; iter++)
      {
         if (bf::is_regular(iter->status()))
         {
            std::cout << (*iter).string() << std::endl;
         }
      }
   }

   return 0;
}
{% endhighlight %}

Program przegląda rekursywnie katalog test_path i wypisuje na standardowe
wyjście wszystkie nazwy plików.

W linii nr. 7 tworzymy obiekt typu boost::path, który definiuje ścieżkę dyskową.
Następnie w linii nr. 9 spradzamy, czy obiekt, na który wskazuje ścieżka
istnieje oraz czy jest to katalog. Następnie tworzymy rekursywny iterator
służący do przeglądania katalogu oraz wypisujemy na wyjście standardowe nazwy
wszystkich plików "zwykłych" (funkcja is_regular).

### Wyrażenia regularne

W skład pakietu [boost](http://boost.org) wchodzi biblioteka _Regex_, która
implementuje wyrażenia regularne w języku C++. Wyrażenia regularne są pewnego
rodzaju językiem służącym do efektywnego oraz prostego przetwarzania łańcuchów
znaków.

Pełny opis składni wyrażeń regularnych można znaleźć w dokumentacji biblioteki
[Boost::Regex](http://www.boost.org/doc/libs/1_44_0/libs/regex/doc/html/index.html).

#### Porównywanie łańcuchów znaków

Poniżej znajduje się przykład porównania danego łańcucha z wyrażeniem regularnym
oraz odwoływanie się do wybranych części łańcucha.

{% highlight cpp linenos %}
#include <boost/regex.hpp>

/*
 * ...
 */

boost::regex regex("^(\\d{4})-(\\d{2})-(\\d{2})$");
boost::smatch matches;
std::string text = "2010-03-12";

if (boost::regex_match(text, matches, regex))
{
   printf("%s\n", matches[1].str().c_str());
}

/*
 * ...
 */

{% endhighlight %}

W linii nr. 7 tworzymy obiekt wyrażenia regularnego. Wyrażenie to definiuje
łańcuch znaków w formie `dddd-dd-dd`, gdzie literka _d_ oznacza cyfrę.

W linii nr. 8 tworzymy obiekt, w którym zostaną zapisane odniesienia do
wyszczególnionych części łańcucha. Wyszczególnione części łańcucha znaków są
określone w wyrażeniu regularnym parami nawiasów okrągłych '()'.

W linii jedenastej wywołujemy funkcję `regex_match`, która sprawdza, czy dany
łańcuch (`text`) pasuje do wyrażenia regularnego `regex`. Dodatkowo funkcja
zapisuje w zmiennej `matches` wyszczególnione części wyrażenia regularnego.

Jeśli łańcuch znaków pasuje do wyrażenia regularnego to w linii 13 wypisujemy
pierwszą grupę znaków (pierwsze 4 cyfry w łańcuchu znaków) na wyjście
standardowe. Należy zauważyć, że pierwsza grupa znajduje się pod indeksem 1 w
zmiennej `matches`.

#### Konwersja łańcuchów

Poniżej znajduje się przykład użycia biblioteki w celu konwersji łańcucha znaków
z jednego formatu na inny.

{% highlight cpp linenos %}
#include <boost/regex.hpp>

std::string convert_date(const std::string &date)
{
   boost::regex regex("^(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2}):(\\d{2})$");
   const std::string format("\\1_\\2_\\3_\\4_\\5_\\6");

   return regex_replace(date, regex, format, boost::format_no_copy);
}
{% endhighlight %}

Zadaniem przedstawionej w przykładzie funkcji `convert_date` jest zmiana formatu
zapisanej daty z postaci "2010-03-30 10:30:00" na "2010_03_30_10_30_00".

W linii nr.5  definiujemy wyrażenie regularne, do którego będą dopasowywane
części (lub całość) łańcucha wejściowego.

W linii nr. 6 tworzymy łańcuch definiujący format, na który należy
przekonwertować dopasowane części łańcucha wejściowego. Cyfry poprzedzone
slashami są indeksami odnoszącymi się do części łańcuchów dopasowanych w
nawiasach wyrażenia regularnego.

W linii nr. 7 wywołujemy funkcję `regex_replace`, która konwertuje łańcuch
wejściowy na nowy format.
