from main import total_por_categoria


def test_suma_por_categoria():
    gastos = [
        {"fecha": "2026-09-01", "categoria": "comida", "monto": 10},
        {"fecha": "2026-09-02", "categoria": "comida", "monto": 5},
        {"fecha": "2026-09-02", "categoria": "estudio", "monto": 7},
    ]

    assert total_por_categoria(gastos) == {"comida": 15, "estudio": 7}