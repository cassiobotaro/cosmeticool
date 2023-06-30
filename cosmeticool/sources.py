import csv
from typing import Protocol, TypeAlias

Dataset: TypeAlias = list[list[str]]


# Protocol for data sources
class DataSource(Protocol):
    def read_data(self) -> Dataset:
        ...


# CSV data source
class CSVDataSource:
    def __init__(self, filename: str):
        self.filename = filename

    def read_data(self) -> Dataset:
        data = []
        with open(self.filename) as file:
            reader = csv.reader(file)
            for row in reader:
                data.append(row)
        return data


# TSV data source
class TSVDataSource:
    def __init__(self, filename: str):
        self.filename = filename

    def read_data(self) -> Dataset:
        data = []
        with open(self.filename) as file:
            reader = csv.reader(file, delimiter="\t")
            for row in reader:
                data.append(row)
        return data
