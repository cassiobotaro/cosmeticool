import argparse

from cosmeticool.metrics import (
    AveragePriceMetric,
    TopSellingProductMetric,
    TotalSalesMetric,
)
from cosmeticool.outputs import (
    CSVOutputGenerator,
    JSONOutputGenerator,
    MarkdownOutputGenerator,
)
from cosmeticool.reports import ReportGenerator
from cosmeticool.sources import CSVDataSource, DataSource, TSVDataSource


def parse_args():
    parser = argparse.ArgumentParser(description="Cosmetic Sales Analyzer")
    parser.add_argument(
        "filename", type=str, help="Path to the data file (CSV or TSV)"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="csv",
        choices=["csv", "json", "md"],
        help="Output format: csv, json, md (default: csv)",
    )
    return parser.parse_args()


def create_data_source(filename: str) -> DataSource:
    if filename.endswith(".csv"):
        return CSVDataSource(filename)
    elif filename.endswith(".tsv"):
        return TSVDataSource(filename)
    else:
        raise ValueError("Unsupported file extension.")


def create_output_generator(output_format: str):
    if output_format == "csv":
        return CSVOutputGenerator()
    elif output_format == "json":
        return JSONOutputGenerator()
    elif output_format == "md":
        return MarkdownOutputGenerator()
    else:
        raise ValueError("Unsupported output format.")


def main():
    args = parse_args()

    data_source = create_data_source(args.filename)
    output_generator = create_output_generator(args.output)

    metrics = [
        TotalSalesMetric(),
        AveragePriceMetric(),
        TopSellingProductMetric(),
    ]

    report_generator = ReportGenerator(metrics, output_generator)

    data = data_source.read_data()
    report_generator.generate_report(data)


if __name__ == "__main__":
    main()
