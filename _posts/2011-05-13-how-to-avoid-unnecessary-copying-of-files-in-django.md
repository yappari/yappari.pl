---
layout: post

author: rczajka
title: Jak uniknąć zbędnego kopiowania plików w Django
---

Załóżmy, że mamy w Django model z polem typu FileField. Zdarza się, że chcemy
tam zapisać duży plik, który mamy już na dysku. W moim przypadku chodzi o
kilkusetmegowe pliki, które trafiają na lokalny dysk poza-djangowymi drogami.
Zapisanie takiego pliku „po bożemu” spowoduje, że plik zostanie skopiowany –
zupełnie bez sensu. Chcielibyśmy, żeby plik nie kopiował się, a tylko co
najwyżej przesunął – albo w ogóle został na miejscu.

Prześledźmy, co się dzieje, kiedy zapisujemy plik w polu.

{% highlight python linenos %}
field.save(name, content)
{% endhighlight %}

Wywołujemy w ten sposób [metodę save klasy
django.db.models.fields.files.FieldsFile](http://code.djangoproject.com/browser/django/tags/releases/1.3/django/db/models/fields/files.py#L92),
gdzie czytamy z kolei:

{% highlight python linenos %}
self.name = self.storage.save(name, content)
{% endhighlight %}

Jest to odwołanie do metody
[save](http://code.djangoproject.com/browser/django/tags/releases/1.3/django/core/files/storage.py#L49)
z klasy django.core.files.storage.Storage, która wywołuje [metodę
_save](http://code.djangoproject.com/browser/django/tags/releases/1.3/django/core/files/storage.py#L178),
w której widzimy:

{% highlight python linenos %}
# This file has a file path that we can move.
if hasattr(content, 'temporary_file_path'):
    file_move_safe(content.temporary_file_path(), full_path)
    content.close()
{% endhighlight %}

I to jest to, o co chodzi, bo
[django.core.files.move.file_move_safe](http://code.djangoproject.com/browser/django/tags/releases/1.3/django/core/files/move.py#L38)
przesuwa plik w możliwie leniwy sposób: jeśli nie trzeba, to nie rusza, jeśli
można (jest na tej samej partycji) to przez os.rename, i na koniec ewentualnie
kopiując.

Potrzebujemy więc opakować nasz plik w obiekt z metodą temporary_file_path – i
dodatkowo z metodą close, która jest wykonywana po przeniesieniu pliku.
Zdefiniujemy więc sobie odpowiednią podklasę klasy
[UploadedFile](http://code.djangoproject.com/browser/django/tags/releases/1.3/django/core/files/uploadedfile.py#L19).

{% highlight python linenos %}
from django.core.files.uploadedfile import UploadedFile

class ExistingFile(UploadedFile):
    """ It's already on disk - avoid unnecessary copying. """
    def __init__(self, path, *args, **kwargs):
        self.path = path
        return super(ExistingFile, self).__init__(*args, **kwargs)

    def temporary_file_path(self):
        return self.path

    def close(self):
        pass
{% endhighlight %}
