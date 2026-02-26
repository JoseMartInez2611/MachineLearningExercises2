"""
/////////////////////////////////////////////////////
Ejercicios Numpy
/////////////////////////////////////////////////////
"""

import numpy as np

"""
1. Crea un array con los números del 1 al 10 y:
a) Calcula la suma total
b) Calcula el promedio
c) Eleva todos los elementos al cuadrado

"""


def exercise_1(array: list):
    # a) Calcula la suma total
    total_sum = np.sum(array)

    # b) Calcula el promedio
    average = np.mean(array)

    # c) Eleva todos los elementos al cuadrado
    squared_array = np.square(array)

    return total_sum, average, squared_array


"""
2. Dados

a=np.array([2,4,6,8])
b=np.array([1,3,5,7])

a) Realiza suma, resta y multiplicación
b) Divide a entre b
c) Calcula a elevado al cubo
d) Calcula b elevado al cubo

"""


def exercise_2(a: list, b: list):
    # a) Realiza suma, resta y multiplicación
    sum_result = np.add(a, b)
    sub_result = np.subtract(a, b)
    mul_result = np.multiply(a, b)

    # b) Divide a entre b
    div_result = np.divide(a, b)

    # c) Calcula a elevado al cubo
    a_cubed = np.power(a, 3)

    # d) Calcula b elevado al cubo
    b_cubed = np.power(b, 3)

    return sum_result, sub_result, mul_result, div_result, a_cubed, b_cubed


"""
3. Crea una matriz 3x3 con números del 1 al 9 usando reshape().
a) Calcula la suma por filas
b) Calcula la suma por columnas
c) Encuentra el valor máximo

"""


def exercise_3():
    # Crea una matriz 3x3 con números del 1 al 9 usando reshape()
    matrix = np.array(range(1, 10)).reshape(3, 3)

    # a) Calcula la suma por filas
    sum_by_rows = np.sum(matrix, axis=1)

    # b) Calcula la suma por columnas
    sum_by_columns = np.sum(matrix, axis=0)

    # c) Encuentra el valor máximo
    max_value = np.max(matrix)

    return sum_by_rows, sum_by_columns, max_value, matrix


"""
4. Crea:

A = np.array([[1],[2],[3]])
B = np.array([10,20,30])

a) Realiza la suma A + B

"""


def exercise_4(a: list, b: list):
    # Crea A y B
    A = np.array(a).reshape(-1, 1)  # Convertir a columna
    B = np.array(b)

    # a) Realiza la suma A + B
    result = A + B

    return result


"""
5. Crea un array con valores [1, 4, 9, 16, 25]
a) Calcula la raíz cuadrada
b) Calcula el logaritmo natural
c) Calcula la exponencia

"""


def exercise_5(array: list):
    # a) calcula la raiz cuadrada
    sqrt_array = np.sqrt(array)

    # b) calcula el logaritmo natural
    log_array = np.log(array)

    # c) calcula la exponencia
    exp_array = np.exp(array)

    return sqrt_array, log_array, exp_array


"""
6. Genera 100 números aleatorios entre 0 y 50.
a) Calcula media
b) Desviación estándar
c) Percentil 90
d) Varianza

"""


def exercise_6():
    # Genera 100 números aleatorios entre 0 y 50
    random_numbers = np.random.uniform(0, 50, 100)

    # a) Calcula media
    mean = np.mean(random_numbers)

    # b) Desviación estándar
    std_dev = np.std(random_numbers)

    # c) Percentil 90
    percentile_90 = np.percentile(random_numbers, 90)

    # d) Varianza
    variance = np.var(random_numbers)

    return mean, std_dev, percentile_90, variance, random_numbers


""""
7. Dado:
a = np.array([5,12,7,18,3,21])
a) Extrae los números mayores que 10
b) Reemplaza los números menores que 10 por 0

"""


def exercise_7():
    a = np.array([5, 12, 7, 18, 3, 21])

    # a) Extrae los números mayores que 10
    greater_than_10 = a[a > 10]

    # b) Reemplaza los números menores que 10 por 0
    modified_array = np.where(a < 10, 0, a)

    return greater_than_10, modified_array


"""
8. Dada la matriz:

A=np.array([[4,2],[1,3]])

a) Calcula el determinante
b) Calcula la inversa
c) Calcula valores propios

"""


def exercise_8():
    A = np.array([[4, 2], [1, 3]])

    # a) Calcula el determinante
    determinant = np.linalg.det(A)

    # b) Calcula la inversa
    inverse = np.linalg.inv(A)

    # c) Calcula valores propios
    eigenvalues, eigenvectors = np.linalg.eig(A)

    return determinant, inverse, eigenvalues, eigenvectors


"""
9. Resuelve el sistema de ecuaciones:
2x + y = 5
x + 3y = 6
Usa np.linalg.solve().

"""


def exercise_9():
    # Coeficientes de las variables
    coeficents = np.array([[2, 1], [1, 3]])

    # Resultados de las ecuaciones
    results = np.array([5, 6])

    # Resuelve el sistema de ecuaciones
    solution = np.linalg.solve(coeficents, results)

    return solution, coeficents, results


"""
10. Crea:

A=np.array([[1,2],[3,4]])

B=np.array([[5,6],[7,8]])

a) Multiplica elemento a elemento
b) Multiplica matricialmente

"""


def exercise_10():
    matrix_a = np.array([[1, 2], [3, 4]])
    matrix_b = np.array([[5, 6], [7, 8]])

    # a) Multiplica elemento a elemento
    elementwise_product = np.multiply(matrix_a, matrix_b)

    # b) Multiplica matricialmente
    matrix_product = np.dot(matrix_a, matrix_b)

    return elementwise_product, matrix_product, matrix_a, matrix_b
