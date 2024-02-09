import pytest
from gendiff import generate_diff


@pytest.fixture
def get_expect_result_flat():
    with open('tests/fixtures/result_flat.txt') as res_file:
        return res_file.read()


@pytest.fixture
def get_expect_result():
    with open('tests/fixtures/result.txt') as res_file:
        return res_file.read()


def test_json_flat(get_expect_result_flat):
    result = generate_diff('tests/fixtures/file1_flat.json', 'tests/fixtures/file2_flat.json', 'stylish')
    assert result == get_expect_result_flat


def test_yaml_flat(get_expect_result_flat):
    result = generate_diff('tests/fixtures/file1_flat.yaml', 'tests/fixtures/file2_flat.yaml', 'stylish')
    assert result == get_expect_result_flat


def test_json(get_expect_result):
    result = generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'stylish')
    assert result == get_expect_result
