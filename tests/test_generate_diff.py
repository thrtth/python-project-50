import pytest
from gendiff import generate_diff


@pytest.fixture
def get_expect_result_flat():
    with open('tests/fixtures/result_flat.txt') as res_file:
        return res_file.read()


@pytest.fixture
def get_expect_result_stylish():
    with open('tests/fixtures/result_stylish.txt') as res_file:
        return res_file.read()


@pytest.fixture
def get_expect_result_plain():
    with open('tests/fixtures/result_plain.txt') as res_file:
        return res_file.read()


@pytest.fixture
def get_expect_result_json():
    with open('tests/fixtures/result_json.txt') as res_file:
        return res_file.read()


def test_json_flat(get_expect_result_flat):
    result = generate_diff('tests/fixtures/file1_flat.json',
                           'tests/fixtures/file2_flat.json',
                           'stylish')
    assert result == get_expect_result_flat


def test_yaml_flat(get_expect_result_flat):
    result = generate_diff('tests/fixtures/file1_flat.yaml',
                           'tests/fixtures/file2_flat.yaml',
                           'stylish')
    assert result == get_expect_result_flat


def test_json_stylish(get_expect_result_stylish):
    result = generate_diff('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json',
                           'stylish')
    assert result == get_expect_result_stylish


def test_yaml_stylish(get_expect_result_stylish):
    result = generate_diff('tests/fixtures/file1.yaml',
                           'tests/fixtures/file2.yaml',
                           'stylish')
    assert result == get_expect_result_stylish


def test_json_plain(get_expect_result_plain):
    result = generate_diff('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json',
                           'plain')
    assert result == get_expect_result_plain


def test_yaml_plain(get_expect_result_plain):
    result = generate_diff('tests/fixtures/file1.yaml',
                           'tests/fixtures/file2.yaml',
                           'plain')
    assert result == get_expect_result_plain


def test_json_json(get_expect_result_json):
    result = generate_diff('tests/fixtures/file1.json',
                           'tests/fixtures/file2.json',
                           'json')
    assert result == get_expect_result_json


def test_yaml_json(get_expect_result_json):
    result = generate_diff('tests/fixtures/file1.yaml',
                           'tests/fixtures/file2.yaml',
                           'json')
    assert result == get_expect_result_json
