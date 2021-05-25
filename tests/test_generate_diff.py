# -*- coding:utf-8 -*-

from gendiff.generate_diff import generate_diff

PATH_TO_JSON_1_FILE = 'tests/fixtures/json_1st_file.json'
PATH_TO_JSON_2_FILE = 'tests/fixtures/json_2nd_file.json'
PATH_TO_JSON_RESULT_FILE = 'tests/fixtures/json_result_file.txt'


def test_generate_diff():

    result_from_generate_diff = generate_diff(
        PATH_TO_JSON_1_FILE,
        PATH_TO_JSON_2_FILE,
    )

    f = open(PATH_TO_JSON_RESULT_FILE)

    result_from_json_file = f.read()

    assert result_from_generate_diff == result_from_json_file
