"""
Решил использовать классы лишь для обозначения группы функций
(фильтрация даты, компиляция вывода)
"""

from typing import Any

from .registry import register_report
from .contract import BaseReport
from .config import *


@register_report
class Clickbait(BaseReport):
    name = 'clickbait'

    @staticmethod
    def data_filtration(row: dict[str, Any]) -> bool:
        try:
            crt = float(row.get('ctr') or 0)
            rate = float(row.get('retention_rate') or 0)

            return crt > clickbait_threshold_crt and rate < clickbait_threshold_rate

        except (ValueError, TypeError, KeyError):
            return False

    @staticmethod
    def output_compilation(row: dict[str, Any]) -> dict[str, Any]:
        result = {  # Создает запись с необходимыми колонками
            key: row[key]
            for key in clickbait_output_headers
            if key in row
        }

        return result

    @staticmethod
    def output_sorting(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        try:
            data = sorted(  # Сортировка по убыванию
                data,
                key=lambda x: x[clickbait_output_sort_column],
                reverse=clickbait_output_sort_reverse
            )

        except (TypeError, KeyError):
            pass

        return data
