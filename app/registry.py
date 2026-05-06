from typing import Type

from .contract import BaseReport


REPORT_REGISTRY: dict[str, Type[BaseReport]] = {}


def register_report(report_class: Type[BaseReport]) -> Type[BaseReport]:
    REPORT_REGISTRY[report_class.name] = report_class
    return report_class
