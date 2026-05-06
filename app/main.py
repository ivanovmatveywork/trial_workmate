import sys

from .registry import REPORT_REGISTRY
from .utils import *


def start(files_path: list[str], report_name: str) -> None:
    data = files_reading(files_path=files_path)                     # Получение данных

    try:
        report_class = REPORT_REGISTRY[report_name]                 # Определение отчета

    except KeyError:
        print('ОШИБКА! Отчет не найден.', file=sys.stderr)
        sys.exit(2)

    result = data_processing(report_class=report_class, data=data)  # Анализ данных
    result = output_normalization(data=result)                      # Нормализация вывода результатов

    print(result)
