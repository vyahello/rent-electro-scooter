[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Build Status](https://travis-ci.org/vyahello/rent-electro-scooter.svg?branch=master)](https://travis-ci.org/vyahello/rent-electro-scooter)
[![Forks](https://img.shields.io/github/forks/vyahello/rent-electro-scooter)](https://github.com/vyahello/rent-electro-scooter/network/members)
[![Stars](https://img.shields.io/github/stars/vyahello/rent-electro-scooter)](https://github.com/vyahello/rent-electro-scooter/stargazers)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

[![PyPI version shields.io](https://img.shields.io/pypi/v/rent-electro-scooter.svg)](https://pypi.python.org/pypi/rent-electro-scooter/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/rent-electro-scooter.svg)](https://pypi.python.org/pypi/rent-electro-scooter/)

# Rent electro scooter

> This is a regular CLI application for renting electro-scooters. 
>
> It uses **SQLAlchemy** API as a database core with ORM (Object Relational Mapper) support.

## Tools
- python 3.6 | 3.7 | 3.8
- [sqlalchemy](https://www.sqlalchemy.org)
- code analysis
  - [pytest](https://pypi.org/project/pytest/)
  - [black](https://black.readthedocs.io/en/stable/)
  - [pylint](https://www.pylint.org/)
  - [flake8](http://flake8.pycqa.org/en/latest/)

## Usage
```bash
****************************************************************************************************
******************************** Electro scooter rental application ********************************
****************************************************************************************************

Please choose a command, [r]ent, [a]vailable, [l]ocate, [h]istory, [q]uit:
```

## Installation

Please run following script to obtain latest package from PYPI:
```bash
➜ pip install scooter-rental
```

Then please launch following tool from your environment:
```bash
➜ scooter-rental
...
```

## Source code

To be able to run source code please execute command below:

```bash
➜ python -m scooter
...
```

## Development notes

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `pylint`, `flake8`) and unittests (`pytest`) will be run automatically
after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
➜ ./analyse-code.sh
```

### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – Volodymyr Yahello

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
3. `pip install -r requirements-dev.txt` to install all development project dependencies