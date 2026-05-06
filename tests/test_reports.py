import pytest

from app.reports import *


def test_reports_data_filtration_true():
    inputs = {'ctr': 16, 'retention_rate': 20}
    output = True

    result = Clickbait.data_filtration(row=inputs)
    assert result == output


def test_reports_data_filtration_false_crt():
    inputs = {'ctr': 1, 'retention_rate': 20}
    output = False

    result = Clickbait.data_filtration(row=inputs)
    assert result == output


def test_reports_data_filtration_false_rate():
    inputs = {'ctr': 16, 'retention_rate': 50}
    output = False

    result = Clickbait.data_filtration(row=inputs)
    assert result == output


def test_reports_data_filtration_false_both():
    inputs = {'ctr': 1, 'retention_rate': 50}
    output = False

    result = Clickbait.data_filtration(row=inputs)
    assert result == output


def test_reports_output_compilation():
    inputs = {'title': 'One', 'ctr': 16, 'retention_rate': 20, 'views': 100}
    output = {'title': 'One', 'ctr': 16, 'retention_rate': 20}

    result = Clickbait.output_compilation(row=inputs)
    assert result == output


def test_reports_output_sorting():
    inputs = [{'ctr': 8, 'retention_rate': 16}, {'ctr': 50, 'retention_rate': 20}, {'ctr': 30, 'retention_rate': 10}]
    output = [{'ctr': 50, 'retention_rate': 20}, {'ctr': 30, 'retention_rate': 10}, {'ctr': 8, 'retention_rate': 16}]

    result = Clickbait.output_sorting(data=inputs)
    assert result == output
