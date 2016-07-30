# python-mystem
CFFI bindings to Yandex.Mystem library  
It's not well tested, so prepare yourself for hallucinations, memory leaks and so on.

# Install
```bash
$ pip install mystem
```

# Usage
```
from mystem import (analyze,
                    Grammeme)

with analyze("мадрид") as lemms:
    print("Lemms count:", len(lemms))
    for n, lemma in enumerate(lemms):
        print("Lemma #{0}: '{1}'".format(n, lemma))
        print("Quality:", lemma.quality)
        print("Is Geo object:", Grammeme.Geo in lemma.stem_grammemes)
        print("Avaible lemma forms:", len(lemma.forms))
        print("First lemma form: '{0}'".format(lemma.forms[0]))

# Will print something like that:
"""
Lemms count: 1
Lemma #0: 'мадрид'
Quality: Quality.Dictionary
Is Geo object: True
Avaible lemma forms: 10
First lemma form: 'мадрид'
"""

```

# License
`python-mystem` code is reliased under MIT license, but Yandex.Mystem have their own EULA, that you must accept.
