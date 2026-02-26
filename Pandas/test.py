import pandas as pd
import Pandas.exercises as exercises


# Ejercicio 1
def test_exercise_1(df: pd.DataFrame):
    print("\nEjercicio 1: \nNueva Columna con Edad Triplicada:\n")
    print(exercises.exercise_1(df))


# Ejercicio 2
def test_exercise_2(df: pd.DataFrame):
    print("\nEjercicio 2: \nNueva Columna que Indica si es Mayor de Edad:\n")
    print(exercises.exercise_2(df))


# Ejercicio 3
def test_exercise_3(df: pd.DataFrame):
    print("\nEjercicio 3: \nNueva Columna que Clasifica el Salario:\n")
    print(exercises.exercise_3(df))


# Ejercicio 4
def test_exercise_4(df: pd.DataFrame):
    print(
        "\nEjercicio 4: \nNueva Columna que Indica si el Nombre Tiene Más de 4 Letras:\n"
    )
    print(exercises.exercise_4(df))


# Ejercicio 5
def test_exercise_5(df: pd.DataFrame):
    print("\nEjercicio 5: \nAumento del 10% al Salario a Mayores de Edad :\n")
    print(exercises.exercise_5(df))


# Ejercicio 6
def test_exercise_6(df: pd.DataFrame):
    print("\nEjercicio 6: \nTop 3 Mayores Salarios:\n")
    print(exercises.exercise_6(df))


# Ejercicio 7
def test_exercise_7(df: pd.DataFrame):
    print("\nEjercicio 7: \nDatos relevantes:\n")
    average_age, max_salary, person_count = exercises.exercise_7(df)

    print(f"Promedio de Edad: {average_age}")
    print(f"Máximo Salario: {max_salary}")
    print(f"Cantidad de Personas: {person_count}")


def run_tests():
    separator = "//////////////////////////////////////////////"
    data = {
        "nombre": ["Ana", "Luis", "Carlos", "Marta", "Sofia"],
        "edad": [17, 25, 32, 15, 45],
        "salario": [800, 1500, 2000, 500, 3000],
    }

    df = pd.DataFrame(data)

    print("Dataframe Original:")
    print(df)
    print(separator)
    test_exercise_1(df)
    print(separator)
    test_exercise_2(df)
    print(separator)
    test_exercise_3(df)
    print(separator)
    test_exercise_4(df)
    print(separator)
    test_exercise_5(df)
    print(separator)
    test_exercise_6(df)
    print(separator)
    test_exercise_7(df)
    print(separator)
