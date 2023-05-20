from typing import Any

raio = float(input("Informe o raio: "))


def calcula_area():
    area: float | Any = 3.14 * (raio * 2)
    print(f"A área do círculo é:{area:.2f}!")


if __name__ == "__main__":
    calcula_area()
