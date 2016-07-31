from setuptools import setup

setup(**{
  "name": "mystem",
  "py_modules": ["mystem"],
  "url": "https://github.com/dveselov/python-mystem",
  "author": "Dmitry Veselov",
  "author_email": "d.a.veselov@yandex.ru",
  "version": "0.1.0",
  "description": "CFFI bindings to Yandex.Mystem",
  "license": "MIT / Yandex License",
  "classifiers": (
    "Intended Audience :: Developers",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: Implementation :: CPython",
  ),
  "install_requires": [
    "cffi==1.7.0",
  ],
})
