from cosmeticool.metrics import Metric
from cosmeticool.outputs import OutputGenerator
from cosmeticool.sources import Dataset


class ReportGenerator:
    def __init__(
        self, metrics: list[Metric], output_generator: OutputGenerator
    ):
        self.metrics = metrics
        self.output_generator = output_generator

    def generate_report(self, data: Dataset) -> None:
        report = {}
        for metric in self.metrics:
            metric_name = metric.__class__.__name__
            report[metric_name] = metric.calculate(data)

        self.output_generator.generate_output(report)
