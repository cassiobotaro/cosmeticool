import csv
import json
from typing import Any, Protocol, TypeAlias

ReportData: TypeAlias = dict[str, Any]


class OutputGenerator(Protocol):
    def generate_output(self, report: ReportData) -> None:
        ...


class CSVOutputGenerator:
    def generate_output(self, report: ReportData) -> None:
        with open("report.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for metric, value in report.items():
                writer.writerow([metric, value])


class JSONOutputGenerator:
    def generate_output(self, report: ReportData) -> None:
        with open("report.json", "w") as file:
            json.dump(report, file)


class MarkdownOutputGenerator:
    def generate_output(self, report: ReportData) -> None:
        with open("report.md", "w") as file:
            file.write("# Report\n\n")
            for metric, value in report.items():
                file.write(f"- {metric}: {value}\n")
