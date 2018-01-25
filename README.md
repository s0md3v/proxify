# Proxify [![python](https://img.shields.io/badge/Python-universal-white.svg?style=style=flat-square)](https://www.python.org/downloads/) ![version](https://img.shields.io/badge/Version-v1_(stable)-blue.svg?style=style=flat-square) [![license](https://img.shields.io/badge/License-GPL_3-orange.svg?style=style=flat-square)](https://github.com/UltimateHacke/XSStrike/blob/master/license.txt)

<img src='https://i.imgur.com/AidfpCt.png' />

Proxify is a python module for dumping usable proxies.

## Documentation

The proxies returned by <b>proxify</b> are in following format:
```
protocol://ip_address:port
```
For example,
```
http://127.0.0.1:8080
```
To get 1 proxy you can simply do this:
``` python
import proxify
proxy = proxify.one()
```
<hr />

To get many proxies, do this:
``` python
import proxify
proxy = proxify.many()
```
<hr />

To dump a specific number of proxies, lets say '5'. You can do this:
``` python
import proxify
proxy = proxify.get(5)
```

### Note
The many() function dumps 300 proxies which is also the maximum number of proxies you can dump with get() function. If you specify a number large than 300, it will automatically become 300.<br>
The one() function returns a string while many() and get() return a list.
