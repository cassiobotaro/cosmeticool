# Protocol for metrics
from typing import Any, Protocol

from cosmeticool.sources import Dataset


class Metric(Protocol):
    def calculate(self, data: Dataset) -> Any:
        ...


class TotalSalesMetric:
    def calculate(self, data: Dataset) -> float:
        total_sales = 0.0
        for row in data:
            total_sales += float(
                row[2]
            )  # Assuming sales value is in the third column
        return total_sales


class AveragePriceMetric:
    def calculate(self, data: Dataset) -> float:
        total_price = 0.0
        num_products = len(data)
        for row in data:
            total_price += float(
                row[3]
            )  # Assuming price value is in the fourth column
        return total_price / num_products


class TopSellingProductMetric:
    def calculate(self, data: Dataset) -> str:
        sales_by_product = {}
        for row in data:
            product = row[1]  # Assuming product name is in the second column
            sales = float(
                row[2]
            )  # Assuming sales value is in the third column
            if product in sales_by_product:
                sales_by_product[product] += sales
            else:
                sales_by_product[product] = sales

        top_product = max(sales_by_product, key=sales_by_product.get)
        return top_product
