import pytest

from tests.paths import TEST_DATA_DIR

from app.main import start


def test_main_start(capsys):
    input_file_one = TEST_DATA_DIR / 'stats1.csv'
    input_file_two = TEST_DATA_DIR / 'stats2.csv'

    inputs_files_path = [input_file_one, input_file_two]
    inputs_report_name = 'clickbait'
    output_path = TEST_DATA_DIR / 'test_main_start_output.csv'

    start(files_path=inputs_files_path, report_name=inputs_report_name)

    with open(output_path, encoding='utf-8') as file:
        expected = file.read()

    result = capsys.readouterr().out.strip()
    assert result == expected.strip()
