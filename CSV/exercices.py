"""
/////////////////////////////////////////////////////
Ejercicios CSV
/////////////////////////////////////////////////////
"""

import csv

FILE_NOT_FOUND_ERROR = "Archivo no encontrado"

"""
1. Leer un archivo notas.txt que contiene números (uno por línea).
Calcular el promedio manejando:
    ● Archivo inexistente
    ● Líneas que no sean números
"""


def exercise_1(route: str):
    try:
        with open(route, "r", encoding="utf-8") as file:
            digits = [int(line.strip()) for line in file if line.strip().isdigit()]

        return sum(digits) / len(digits) if digits else None

    except FileNotFoundError:
        print(FILE_NOT_FOUND_ERROR)
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None


"""
2. Leer un archivo personas.csv con columnas:
    ● nombre, edad, ciudad
        ○ Mostrar sólo personas mayores de edad
Manejar:
    ● Archivo inexistente
    ● Edad inválida
"""


def exercise_2(route: str):
    try:
        with open(route, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, skipinitialspace=True)
            header = reader.fieldnames
            filtered_rows = [
                [row[col] for col in header]
                for row in reader
                if row["edad"].isdigit() and int(row["edad"]) >= 18
            ]
        return header, filtered_rows
    except FileNotFoundError:
        print(FILE_NOT_FOUND_ERROR)
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None


"""
3. Contar cuántos registros válidos hay en un CSV que contiene:
    ● producto, precio
        ○ Ignorar precios inválidos.
"""


def exercise_3(route: str):
    try:
        with open(route, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, skipinitialspace=True)
            return sum(
                1
                for row in reader
                if row["precio"].isdigit() and int(row["precio"]) > 0
            )
    except FileNotFoundError:
        print(FILE_NOT_FOUND_ERROR)
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None


"""
4. Leer datos.txt y crear numeros.txt con solo líneas numéricas válidas.
"""


def exercise_4(route: str):
    try:
        with open(route, "r", encoding="utf-8") as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]

        output_route = "CSV/OUTPUT/numeros.txt"
        with open(output_route, "w", newline="", encoding="utf-8") as output:
            writer = csv.writer(output)
            writer.writerows([[n] for n in numbers])
        return output_route
    except FileNotFoundError:
        print(FILE_NOT_FOUND_ERROR)
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")


"""
5. Leer un CSV y verificar que tenga columnas:
    ● nombre, edad, correo
        ○ Si falta alguna, lanzar error.
"""


def exercise_5(route: str, required_columns: list[str]):
    try:
        with open(route, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, skipinitialspace=True)
            for col in required_columns:
                if col not in reader.fieldnames:
                    raise ValueError(f"Falta la columna: {col}")
    except FileNotFoundError:
        print(FILE_NOT_FOUND_ERROR)
        return None
    except ValueError as ve:
        print(ve)
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None


"""
6. Leer un CSV de estudiantes:
    ● nombre, nota1, nota2
        o Calcular promedio
        o Ignorar notas inválidas
        o Guardar aprobados en aprobados.csv
        o Manejar todos los errores posibles
"""


def exercise_6(route: str):
    try:
        with open(route, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, skipinitialspace=True)

            approved_students = []

            for row in reader:
                nombre = row.get("nombre").strip()
                nota1 = row.get("nota1").strip()
                nota2 = row.get("nota2").strip()

                try:
                    n1 = float(nota1)
                    n2 = float(nota2)

                    promedio = (n1 + n2) / 2

                    if promedio >= 60:
                        approved_students.append(
                            {"nombre": nombre, "promedio": round(promedio, 2)}
                        )
                except ValueError:
                    continue

            output_route = "CSV/OUTPUT/aprobados.csv"
            with open(output_route, "w", newline="", encoding="utf-8") as output:
                writer = csv.DictWriter(output, fieldnames=["nombre", "promedio"])
                writer.writeheader()
                writer.writerows(approved_students)

            return output_route
    except FileNotFoundError:
        print(FILE_NOT_FOUND_ERROR)
        return None
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        return None
