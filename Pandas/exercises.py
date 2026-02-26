"""
/////////////////////////////////////////////////////
Ejercicios Pandas
/////////////////////////////////////////////////////
"""

import pandas as pd

"""
1.Crear una columna con la edad triplicada
"""


def exercise_1(df: pd.DataFrame):
    df["edad_triplicada"] = df["edad"] * 3
    return df


"""
2. Crear una columna que indique si es mayor de edad (>= 18)
"""


def exercise_2(df: pd.DataFrame):
    df["mayor_edad"] = df["edad"] >= 18
    return df


"""
3. Clasificar salario como "Bajo", "Medio" o "Alto"
Reglas:
● < 1000 → Bajo
● 1000–1999 → Medio
● = 2000 → Alto
"""


def exercise_3(df: pd.DataFrame):
    def clasify_salary(salary: int):
        if salary < 1000:
            return "Bajo"
        elif 1000 <= salary < 2000:
            return "Medio"
        else:
            return "Alto"

    df["salario_clasificado"] = df["salario"].apply(clasify_salary)
    return df


"""
4. Crear una columna que indique si el nombre tiene más de 4 letras
"""


def exercise_4(df: pd.DataFrame):
    df["nombre_mas_4_letras"] = df["nombre"].str.len() > 4
    return df


"""
5. Aumentar salario en 10% solo a mayores de edad
"""


def exercise_5(df: pd.DataFrame):
    df["salario"] = df.apply(
        lambda row: row["salario"] * 1.1 if row["edad"] >= 18 else row["salario"],
        axis=1,
    )
    return df


"""
6. Mostrar sólo personas con salario mayor
"""


def exercise_6(df: pd.DataFrame):
    df = df.sort_values("salario", ascending=False)
    return df.head(3)


""""
7. Calcular:
● Promedio de edad
● Máximo salario
● Cantidad de personas

"""


def exercise_7(df: pd.DataFrame):
    return df["edad"].mean(), df["salario"].max(), df["nombre"].count()
