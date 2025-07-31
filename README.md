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
.venv/bin/pip install -r requirements.txt
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

### Generating the coverage

To run the test suite and generate the coverage files, run:

```
./run_tests.sh
```

You should then be able to run the FLITSR tool on the output by running:

```
.venv/bin/flitsr coverage.tcm
```

### Extending the example

Currently there is only a rudimentary example, for which the source code is in
`src/main.py`, and the tests are in subdirectories in `test/resources/`. The
tests just contain input that will be given on stdin, as well as the expected
outputs (in the `test/resources/outputs` directory). The `test/conftest.py` file
automatically finds all tests and outputs in the `test/resources`
sub-directories, and the `runner_test.py` file runs each of these inputs as a
test case, comparing the output of the program with the expected output.

To extend this, simply replace the program files in `src`, and the test cases
used in the `test/resources` directories. If you would like to change how the
tests are run, you may also edit `test/runner_test.py` to change how the tests
are run.
