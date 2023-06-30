# Cosmeticool

Cosmeticool is a cosmetic sales report generator.

## Installation

Use the package manager [poetry](https://python-poetry.org/docs/pyproject/) to install cosmeticool.

```bash
poetry install
```

If you are a developer make sure you install [pre-commit](https://pre-commit.com/).


## Usage

The command to use the CLI is `poetry run cosmetic_sales_analyzer <filename> -o <report extension>`.

```shell
poetry run cosmetic_sales_analyzer cosmetic_sales.csv -o md
```

## Tests

```shell
poetry run python -m unittest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
