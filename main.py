import pandas as pd
from rich.console import Console
from rich.table import Table


GASTOS = [
    {"fecha": "2026-09-01", "categoria": "comida", "monto": 25000},
    {"fecha": "2026-09-01", "categoria": "transporte", "monto": 8000},
    {"fecha": "2026-09-02", "categoria": "comida", "monto": 18000},
    {"fecha": "2026-09-03", "categoria": "estudio", "monto": 60000},
    {"fecha": "2026-09-03", "categoria": "transporte", "monto": 8000},
]


def total_por_categoria(gastos: list[dict]) -> dict[str, int]:
    df = pd.DataFrame(gastos)
    return df.groupby("categoria")["monto"].sum().to_dict()


def main() -> None:
    totales = total_por_categoria(GASTOS)

    tabla = Table(title="Gastos por categoria")
    tabla.add_column("Categoria")
    tabla.add_column("Total", justify="right")

    for categoria, total in totales.items():
        tabla.add_row(categoria, f"${total:,}")

    Console().print(tabla)


if __name__ == "__main__":
    main()