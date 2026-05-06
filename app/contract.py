from typing import Protocol, Any


class BaseReport(Protocol):
    name: str  # Название отчета

    @staticmethod
    def data_filtration(row: dict[str, Any]) -> bool:
        """Возвращается True, если запись должна попасть в отчет"""
        ...

    @staticmethod
    def output_compilation(row: dict[str, Any]) -> dict[str, Any]:
        """Создает запись для отчета"""
        ...

    @staticmethod
    def output_sorting(data: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Сортировка записей перед выводом отчета"""
        ...
