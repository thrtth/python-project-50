import os.path
import pytest
from gendiff import generate_diff


def get_fixtures_path():
    return os.path.join(os.path.dirname(__file__), 'fixtures')


@pytest.mark.parametrize("file1, file2, format_name, expected",
                         [("file1.json", "file2.json",
                           "stylish", "result_stylish.txt"),
                          ("file1.yaml", "file2.yaml",
                           "stylish", "result_stylish.txt"),
                          ("file1.json", "file2.json",
                           "plain", "result_plain.txt"),
                          ("file1.yaml", "file2.yaml",
                           "plain", "result_plain.txt"),
                          ("file1.json", "file2.json",
                           "json", "result_json.txt"),
                          ("file1.yaml", "file2.yaml",
                           "json", "result_json.txt")])
def test_generate_diff(file1, file2, format_name, expected):
    with open(os.path.join(get_fixtures_path(), expected)) as res_file:
        expected_result = res_file.read()
    result = generate_diff(os.path.join(get_fixtures_path(), file1),
                           os.path.join(get_fixtures_path(), file2),
                           format_name)
    assert result == expected_result
