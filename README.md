# python-mystem [![Build Status](https://travis-ci.org/dveselov/python-mystem.svg?branch=master)](https://travis-ci.org/dveselov/python-mystem)
CFFI bindings to Yandex.Mystem library  
It's not well tested, so prepare yourself for hallucinations, memory leaks and so on.

# Install
```bash
# Install libmystem-c-binding.so
$ wget https://github.com/yandex/tomita-parser/releases/download/v1.0/libmystem_c_binding.so.linux_x64.zip
$ unzip libmystem_c_binding.so.linux_x64.zip
$ sudo cp libmystem_c_binding.so /usr/lib/
```
```bash
$ pip install mystem
```

# Usage
```python
from mystem import (analyze, Grammeme)

text = "Иван Иванович Иванов приехал в Санкт-Петербург"
for word in text.split(" "):
    with analyze(word) as result:
        print(result[0].form, 
             "({0})".format(result[0]),
             result[0].stem_grammemes, 
             result[0].flex_grammemes
        )


# Will print something like that:
"""
иван (иван) [<Grammeme.Substantive: 136>, <Grammeme.FirstName: 155>, <Grammeme.Masculine: 192>, <Grammeme.Animated: 201>] [[<Grammeme.Nominative: 165>, <Grammeme.Singular: 174>]]
иванович (иванович) [<Grammeme.Substantive: 136>, <Grammeme.Patr: 157>, <Grammeme.Masculine: 192>, <Grammeme.Animated: 201>] [[<Grammeme.Nominative: 165>, <Grammeme.Singular: 174>]]
иванов (иванов) [<Grammeme.Substantive: 136>, <Grammeme.Surname: 156>, <Grammeme.Masculine: 192>, <Grammeme.Animated: 201>] [[<Grammeme.Nominative: 165>, <Grammeme.Singular: 174>]]
приехал (приезжать) [<Grammeme.Verb: 137>, <Grammeme.Intransitive: 206>] [[<Grammeme.Past: 162>, <Grammeme.Singular: 174>, <Grammeme.Indicative: 179>, <Grammeme.Masculine: 192>, <Grammeme.Perfect: 195>]]
в (в) [<Grammeme.Preposition: 135>] [[]]
санкт-петербург (санкт-петербург) [<Grammeme.Substantive: 136>, <Grammeme.Geo: 158>, <Grammeme.Masculine: 192>, <Grammeme.Inanimated: 202>] [[<Grammeme.Accusative: 168>, <Grammeme.Singular: 174>], [<Grammeme.Nominative: 165>, <Grammeme.Singular: 174>]]
"""

```

# License
`python-mystem` code is released under MIT license, but Yandex.Mystem have their own EULA, that you must accept.
