[![Python CI](https://github.com/a-yanovskiy/python-project-lvl2/actions/workflows/pyci.yml/badge.svg)](https://github.com/a-yanovskiy/python-project-lvl2/actions)
[![hexlet-check](https://github.com/a-yanovskiy/python-project-lvl2/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/a-yanovskiy/python-project-lvl2/actions/workflows/hexlet-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/87e61e5ad46a30363ef3/maintainability)](https://codeclimate.com/github/a-yanovskiy/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/87e61e5ad46a30363ef3/test_coverage)](https://codeclimate.com/github/a-yanovskiy/python-project-lvl2/test_coverage)

Find difference between two .json or .yaml files.

[![asciicast](https://asciinema.org/a/wTbglsVGk8Jd9h5fxbkUtjp8K.svg)](https://asciinema.org/a/wTbglsVGk8Jd9h5fxbkUtjp8K)

### json

```commandline
gendiff file1.json file2.json
```

### yaml

```commandline
gendiff file1.yaml file2.yaml
```

# Usage

## Formatters

There are three different views so that you can see the difference between files, to use it you need to use the
flag `-f`.

### Stylish

```commandline
gendiff file1.json file2.json -f stylish
```

Here you may not specify `-f stylish`. It uses by default.

### Plain

```commandline
gendiff file1.json file2.json -f plain
```

### Json

```commandline
gendiff file1.json file2.json -f json
```
