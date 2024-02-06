import pytest

from gendiff import generate_diff


@pytest.fixture
def get_expect_result():
    with open('tests/fixtures/result.txt') as res_file:
        return res_file.read()


def test_json(get_expect_result):
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
    assert result == get_expect_result


def test_yaml(get_expect_result):
    result = generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
    assert result == get_expect_result
