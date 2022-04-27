[![hexlet-check](https://github.com/a-yanovskiy/python-project-lvl2/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/a-yanovskiy/python-project-lvl2/actions/workflows/hexlet-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/87e61e5ad46a30363ef3/maintainability)](https://codeclimate.com/github/a-yanovskiy/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/87e61e5ad46a30363ef3/test_coverage)](https://codeclimate.com/github/a-yanovskiy/python-project-lvl2/test_coverage)

Find difference between two .json or .yaml files.
***
### json
```commandline
gendiff file1.json file2.json
```
### yaml
```commandline
gendiff file1.yaml file2.yaml
```
***
> Warning! There is no way to get difference between files with different formats.
***
# Usage
## Formatters
There are three different views so that you can see the difference between files, to use it you need to use the flag `-f`.

For example, there are two files that we need to compare with each other:

*file1.json*
```json
{
    "host": "hexlet.io",
    "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": false
}
```

*file2.json*
```json
{
    "timeout": 20,
    "verbose": true,
    "host": "hexlet.io"
}
```
### Stylish
```commandline
gendiff file1.json file2.json -f stylish
```
Here you may not specify `-f stylish`. It uses by default.

Here's what it looks like:
```commandline
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```
### Plain
```commandline
gendiff file1.json file2.json -f plain
```
Here's what it looks like:
```commandline
Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true
```
### Json
```commandline
gendiff file1.json file2.json -f json
```
Here's what it looks like:
```commandline
{
  "follow": {
    "body1": false,
    "status": "deleted"
  },
  "host": {
    "body1": "hexlet.io",
    "status": "unchanged"
  },
  "proxy": {
    "body1": "123.234.53.22",
    "status": "deleted"
  },
  "timeout": {
    "body1": 50,
    "body2": 20,
    "status": "replaced"
  },
  "verbose": {
    "body1": true,
    "status": "added"
  }
}
```
***
[![asciicast](https://asciinema.org/a/wTbglsVGk8Jd9h5fxbkUtjp8K.svg)](https://asciinema.org/a/wTbglsVGk8Jd9h5fxbkUtjp8K)
