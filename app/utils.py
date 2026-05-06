"""
В ТЗ указано, что программа должна создавать единый отчет по всем таблицам.
Подразумеваю, что все отчеты будут лишь складывать таблицы и не сопоставляться.
По этому решил вынести чтение в отдельную функцию.

Также предполагаю, что таблицы будут нормализованы и иметь одинаковые колонны.
Так как в ТЗ указано, что все данные нормализованны.
По этому объединю записи в один список.
"""

from typing import Type, Any
import csv
import sys

from tabulate import tabulate

from .contract import BaseReport
from .reports import *


__all__ = ['files_reading', 'data_processing', 'output_normalization']


def _csv_reading(path: str) -> list[dict[str, Any]]:
    try:
        with open(path, encoding='utf-8') as file:  # Открытие файла. UTF-8, ибо Кириллица
            result = list(csv.DictReader(file))     # Чтение записей. Для работы сильно удобнее dict

    except FileNotFoundError:
        print(f'ОШИБКА! Файл {path} не найден.', file=sys.stderr)
        sys.exit(2)

    return result


def files_reading(files_path: list[str]) -> list:
    result = []

    for path in files_path:                 # Для каждого файла
        data_csv = _csv_reading(path=path)  # Получение данных файла
        result += data_csv                  # Добавление данных файла в итоговый список

    return result


def data_processing(report_class: Type[BaseReport], data: list[dict[str, Any]]) -> dict:
    result = []

    for row in data:                                               # Для каждой записи
        if report_class.data_filtration(row=row):                  # Если фильтр пройден
            row_report = report_class.output_compilation(row=row)  # Компиляция выходной записи
            result.append(row_report)                              # Добавление записи в итоговый список

    result = report_class.output_sorting(data=result)              # Сортировка записей

    return result


def output_normalization(data: list[dict[str, Any]]) -> str:
    result = tabulate(data, headers='keys', tablefmt='grid')  # Табличный вид
    return result
