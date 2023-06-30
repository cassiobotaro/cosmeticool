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


class HtmlOutputGenerator:
    def __init__(self):
        self.generated_output = ""

    def generate_output(self, report: ReportData) -> None:
        self.generated_output = "<html><body>"
        self.generated_output += "<h1>Report</h1>"
        self.generated_output += "<table>"
        self.generated_output += "<tr><th>Metric</th><th>Value</th></tr>"
        for metric, value in report.items():
            self.generated_output += (
                f"<tr><td>{metric}</td><td>{value}</td></tr>"
            )
        self.generated_output += "</table>"
        self.generated_output += "</body></html>"

    def get_output(self):
        return self.generated_output
