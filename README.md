# Novenv - automatically handles your virtualenvs

*Novenv* automatically selects the correct python interpreter (global or virtualenv) depending on the current working directory and the occurence of a virtualenv; so you don't have to worry about activating and deactivating virtualenvs - it is done automatically for you.


## Installation

Install *novenv*

```
git clone https://github.com/chaosmail/python-novenv.git
cd python-novenv
python setup.py install
```



## Usage

Run `novenv` in your project root directory to create a new virtualenv; this will be stored in the *.novenv/* directory.

Just run `python` or `pip` in your terminal as you would do it normally.