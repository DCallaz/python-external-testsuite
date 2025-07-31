from pathlib import Path
from pkg_resources import resource_filename


def pytest_generate_tests(metafunc):
    if "test_input_file" in metafunc.fixturenames:
        test_dir = resource_filename('test.resources', 'marking-tests')
        output_dir = resource_filename('test.resources', 'outputs')
        tests = list(Path(test_dir).rglob("*.[tT][xX][tT]"))
        arguments = [(t, Path(output_dir, t.relative_to(test_dir))) for t in
                     tests]
        ids = [str(t.relative_to(test_dir)).replace("/", ".") for t in tests]
        metafunc.parametrize("test_input_file,expected_output_file", arguments,
                             ids=ids)
