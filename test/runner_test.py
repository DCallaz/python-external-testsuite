import pytest
import subprocess
import os

os.chdir("src")


@pytest.fixture
def remove_leading_trailing_ws(str1):
    pass


@pytest.mark.timeout(60)
def test_compute(test_input_file, expected_output_file):
    test_input = open(test_input_file, 'r').read()
    result = subprocess.run(["python3", "main.py", "0"], input=test_input,
                            text=True, stdout=subprocess.PIPE)
    output = result.stdout
    expected_output = open(expected_output_file, 'r').read()
    assert output == expected_output
