import CSV.exercices as exercises


# Ejercicio 1
def test_exercise_1():
    print("\nEjercicio 1:")
    route = "CSV/Data/notas.txt"
    result = exercises.exercise_1(route)
    if result is not None:
        print(f"Promedio de notas: {result}")


# Ejercicio 2
def test_exercise_2():
    print("\nEjercicio 2:")
    route = "CSV/Data/personas.csv"
    header, results = exercises.exercise_2(route)
    if results is not None:
        print("Personas mayores de edad:")
        matrix = [header] + results

        for row in matrix:
            print(row)


# Ejercicio 3
def test_exercise_3():
    print("\nEjercicio 3:")
    route = "CSV/Data/productos.csv"
    result = exercises.exercise_3(route)
    if result is not None:
        print(f"Cantidad de registros válidos: {result}")


# Ejercicio 4
def test_exercise_4():
    print("\nEjercicio 4:")
    route = "CSV/Data/datos.txt"
    output_route = exercises.exercise_4(route)
    if output_route:
        print(f"Archivo numeros.txt creado con números válidos en: {output_route}")


# Ejercicio 5
def test_exercise_5():
    print("\nEjercicio 5:")
    route = "CSV/Data/personas.csv"
    required_columns = ["nombre", "edad", "correo"]
    result = exercises.exercise_5(route, required_columns)
    if result is not None:
        print("El archivo contiene la columnas solicitadas")


# Ejercicio 6
def test_exercise_6():
    print("\nEjercicio 6:")
    route = "CSV/Data/estudiantes.csv"
    output_route = exercises.exercise_6(route)
    if output_route:
        print(
            f"Archivo aprobados.csv creado con los estudiantes con un promedio mayor o igual a 60 en: {output_route}"
        )


def run_tests():
    separator = "\n//////////////////////////////////////////////"

    print(separator)
    test_exercise_1()
    print(separator)
    test_exercise_2()
    print(separator)
    test_exercise_3()
    print(separator)
    test_exercise_4()
    print(separator)
    test_exercise_5()
    print(separator)
    test_exercise_6()
    print(separator)


run_tests()
