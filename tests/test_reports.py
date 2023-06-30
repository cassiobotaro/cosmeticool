import unittest

from cosmeticool.reports import ReportGenerator


class FakeMetric1:
    def calculate(self, data):
        return 500.0


class FakeMetric2:
    def calculate(self, data):
        return 13.39


class FakeOutputGenerator:
    def __init__(self):
        self.generated_output = None

    def generate_output(self, report):
        self.generated_output = report


class ReportGeneratorTestCase(unittest.TestCase):
    def setUp(self):
        self.metrics = [FakeMetric1(), FakeMetric2()]
        self.output_generator = FakeOutputGenerator()
        self.report_generator = ReportGenerator(
            self.metrics, self.output_generator
        )
        self.data = [
            ["1", "Lipstick", "100", "10.99"],
            ["2", "Eyeshadow Palette", "50", "19.99"],
            ["3", "Mascara", "80", "8.99"],
            ["4", "Foundation", "120", "15.99"],
            ["5", "Blush", "70", "12.99"],
        ]

    def test_generate_report(self):
        self.report_generator.generate_report(self.data)

        expected_report = {"FakeMetric1": 500.0, "FakeMetric2": 13.39}
        self.assertEqual(
            self.output_generator.generated_output, expected_report
        )
