import unittest

from cosmeticool.metrics import (
    AveragePriceMetric,
    TopSellingProductMetric,
    TotalSalesMetric,
)


class MetricsTestCase(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.data = [
            ["1", "Lipstick", "100", "10.99"],
            ["2", "Eyeshadow Palette", "50", "19.99"],
            ["3", "Mascara", "80", "8.99"],
            ["4", "Foundation", "120", "15.99"],
            ["5", "Blush", "70", "12.99"],
        ]

    def test_total_sales_metric(self):
        metric = TotalSalesMetric()
        expected_total_sales = 420.0
        total_sales = metric.calculate(self.data)
        self.assertAlmostEqual(total_sales, expected_total_sales)

    def test_average_price_metric(self):
        metric = AveragePriceMetric()
        expected_average_price = 13.79
        average_price = metric.calculate(self.data)
        self.assertAlmostEqual(average_price, expected_average_price, places=2)

    def test_top_selling_product_metric(self):
        metric = TopSellingProductMetric()
        expected_top_product = "Foundation"
        top_product = metric.calculate(self.data)
        self.assertEqual(top_product, expected_top_product)
