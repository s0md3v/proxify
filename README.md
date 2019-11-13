# Proxify [![python](https://img.shields.io/badge/Python-universal-white.svg?style=style=flat-square)](https://www.python.org/downloads/) ![version](<https://img.shields.io/badge/Version-v1_(stable)-blue.svg?style=style=flat-square>) [![license](https://img.shields.io/badge/License-GPL_3-orange.svg?style=style=flat-square)](https://github.com/UltimateHacke/XSStrike/blob/master/license.txt)

<img src='https://i.imgur.com/AidfpCt.png' />

Proxify is a python module for dumping usable proxies.</br>
It supports both python2 and python3 and can be install via pip as follows.

```
pip install proxify
```

## Documentation

The proxies returned by <b>proxify</b> are in following format:

```py
[{
	'ip': '---.---.---.---',
	'port': '------',
	'country': {
		'code': '--',
		'name': '-------'
	},
	'anonymity': '--------',
	'google': True / False,
	'https': True / False,
	'last_update': '--------',
	'url': 'protocol://ip_address:port'
}]
```

To get 1 proxy you can simply do this:

```python
import proxify
proxy = proxify.fetch(count=1)
```

Output:

```
[{
	'ip': '138.36.7.45',
	'port': '40973',
	'country': {
		'code': 'BR',
		'name': 'Brazil'
	},
	'anonymity': 'elite proxy',
	'google': False,
	'https': True,
	'last_update': '1 minute ago',
	'url': 'https://138.36.7.45:40973'
}]
```

<hr />

To get many proxies, do this:

```python
import proxify
proxy = proxify.fetch()
```

Output:

```python
[{
	'ip': '138.36.7.45',
	'port': '40973',
	'country': {
		'code': 'BR',
		'name': 'Brazil'
	},
	'anonymity': 'elite proxy',
	'google': False,
	'https': True,
	'last_update': '1 minute ago',
	'url': 'https://138.36.7.45:40973'
},
....
{
	'ip': '189.51.101.126',
	'port': '39108',
	'country': {
		'code': 'BR',
		'name': 'Brazil'
	},
	'anonymity': 'elite proxy',
	'google': False,
	'https': False,
	'last_update': '3 minutes ago',
	'url': 'http://189.51.101.126:39108'
}]
```

<hr />

To dump a specific number of proxies, lets say '2'. You can do this:

```python
import proxify
proxy = proxify.get(count=2)
```

Output:

```py
[{'ip': '125.26.6.98', 'port': '32385', 'country': {'code': 'TH', 'name': 'Thailand'}, 'anonymity': 'elite proxy', 'google': False, 'https': True, 'last_update': '2 minutes ago', 'url': 'https://125.26.6.98:32385'}, {'ip': '117.58.245.114', 'port': '53985', 'country': {'code': 'BD', 'name': 'Bangladesh'}, 'anonymity': 'elite proxy', 'google': False, 'https': True, 'last_update': '2 minutes ago', 'url': 'https://117.58.245.114:53985'}, {'ip': '103.36.126.14', 'port': '43999', 'country': {'code': 'IN', 'name': 'India'}, 'anonymity': 'elite proxy', 'google': False, 'https': True, 'last_update': '2 minutes ago', 'url': 'https://103.36.126.14:43999'}, {'ip': '181.129.140.226', 'port': '38681', 'country': {'code': 'CO', 'name': 'Colombia'}, 'anonymity': 'elite proxy', 'google': False, 'https': True, 'last_update': '2 minutes ago', 'url': 'https://181.129.140.226:38681'}, {'ip': '114.5.195.226', 'port': '8080', 'country': {'code': 'ID', 'name': 'Indonesia'}, 'anonymity': 'anonymous', 'google': False, 'https': True, 'last_update': '2 minutes ago', 'url': 'https://114.5.195.226:8080'}]

```

**NOTE** The `filter()` function dumps **300** proxies which is also the maximum number of proxies. If you specify a number large than 300, it will automatically become 300.<br>

#### Dependencies

- re
- urllib

Made with ![heart](https://cloud.githubusercontent.com/assets/4301109/16754758/82e3a63c-4813-11e6-9430-6015d98aeaab.png) by <a href=https://twitter.com/s0md3v>Somdev Sangwan</a>
