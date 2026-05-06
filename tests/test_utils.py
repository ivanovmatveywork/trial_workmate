import pytest

from tests.paths import TEST_DATA_DIR

from app.reports import *

from app.utils import *
from app.utils import _csv_reading


def test_utils__csv_reading():
    inputs = TEST_DATA_DIR / 'test_utils__csv_reading_input.csv'
    output = [{'title': 'One', 'ctr': '1_1', 'retention_rate': '1_2'},
              {'title': 'Two', 'ctr': '2_1', 'retention_rate': '2_2'}]

    result = _csv_reading(path=inputs)
    assert result == output


def test_utils_files_reading():
    input_file_one = TEST_DATA_DIR / 'test_utils_files_reading_input_one.csv'
    input_file_two = TEST_DATA_DIR / 'test_utils_files_reading_input_two.csv'

    inputs = [input_file_one, input_file_two]
    output = [{'title': 'One', 'ctr': '1_1', 'retention_rate': '1_2'},
              {'title': 'Two', 'ctr': '2_1', 'retention_rate': '2_2'},
              {'title': 'Three', 'ctr': '3_1', 'retention_rate': '3_2'}]

    result = files_reading(files_path=inputs)
    assert result == output


def test_utils_data_processing():
    inputs_report_class = Clickbait
    inputs_data = [{'title': 'One', 'ctr': '16', 'retention_rate': '30'},
                   {'title': 'Two', 'ctr': '18', 'retention_rate': '25'},
                   {'title': 'Three', 'ctr': '10', 'retention_rate': '20'}]
    output = [{'title': 'Two', 'ctr': '18', 'retention_rate': '25'},
              {'title': 'One', 'ctr': '16', 'retention_rate': '30'}]

    result = data_processing(report_class=inputs_report_class, data=inputs_data)
    assert result == output


def test_utils_output_normalization():
    inputs = [{'ctr': 8, 'retention_rate': 16},
              {'ctr': 50, 'retention_rate': 20},
              {'ctr': 30, 'retention_rate': 10}]
    output_path = TEST_DATA_DIR / 'test_utils_output_normalization_output.txt'

    with open(output_path) as file:
        output = file.read()

    result = output_normalization(data=inputs)
    assert result == output
