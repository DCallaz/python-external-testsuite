# Example Python project running external test-suite

This repository is meant to give an example of how to run coverage collection
and SBFL techniques using a project that contains an external test-suite (e.g.
for an undergraduate project).

## Setup

### Virtual environment

Firstly, it is advised that you use a virtual environment to run this example,
so that you don't clutter your main python installation. To do so, run the
following command:
```
python3 -m venv .venv
```

This command creates the virtual environment `.venv`. Note that this is assumed
in the `run_tests.sh` script.

### Installing requirements

To set up this example, you must install the requirements either using pip or
poetry.

#### Pip install

To use pip, install the packages listed in the `requirements.txt` file using pip
as follows:

```
pip install -r requirements.txt
```

#### Poetry install

If you would instead like to use [Poetry](https://python-poetry.org/docs/)
instead, first install poetry:

```
pip install pipx
pipx install poetry
```

Then install the dependencies:

```
poetry install
```

## Usage
