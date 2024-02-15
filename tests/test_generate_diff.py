import os.path
import pytest
from gendiff import generate_diff


def get_absolute_path(relative_path):
    return os.path.abspath(relative_path)


@pytest.mark.parametrize("file1, file2, format_name, expected",
                         [("tests/fixtures/file1.json", "tests/fixtures/file2.json",
                           "stylish", "tests/fixtures/result_stylish.txt"),
                          ("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml",
                           "stylish", "tests/fixtures/result_stylish.txt"),
                          ("tests/fixtures/file1.json", "tests/fixtures/file2.json",
                           "plain", "tests/fixtures/result_plain.txt"),
                          ("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml",
                           "plain", "tests/fixtures/result_plain.txt"),
                          ("tests/fixtures/file1.json", "tests/fixtures/file2.json",
                           "json", "tests/fixtures/result_json.txt"),
                          ("tests/fixtures/file1.yaml", "tests/fixtures/file2.yaml",
                           "json", "tests/fixtures/result_json.txt")])
def test_generate_diff(file1, file2, format_name, expected):
    with open(get_absolute_path(expected)) as res_file:
        expected_result = res_file.read()
    result = generate_diff(get_absolute_path(file1), get_absolute_path(file2), format_name)
    assert result == expected_result
