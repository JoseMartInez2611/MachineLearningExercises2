import numpy as np

import Exercises

#Ejercicio 1
def test_exercise_1():
    array=list([2,2,2,2,2,2,2,2,2,2])

    total_sum, average, squared_array = Exercises.exercise_1(array)

    print("\nEjercicio 1: \n" \
        "Lista usada:" + str(array) + "\n" \
        "Suma Total: " + str(total_sum) + "\n" \
        "Promedio: " + str(average) + "\n" \
        "Cuadrados: " + str(squared_array)+"\n")
    



#Ejercicio 2
def test_exercise_2():
    a=list([2,4,6,8])
    b=list([1,3,5,7])

    sum_result, sub_result, mul_result, div_result, a_cubed, b_cubed = Exercises.exercise_2(a,b)

    print("\nEjercicio 2: \n" \
        "Lista a:" + str(a) + "\n" \
        "Lista b:" + str(b) + "\n" \
        "Suma: " + str(sum_result) + "\n" \
        "Resta: " + str(sub_result) + "\n" \
        "Multiplicación: " + str(mul_result) + "\n" \
        "División: " + str(div_result) + "\n" \
        "Cubo de a: " + str(a_cubed) + "\n" \
        "Cubo de b: " + str(b_cubed)+"\n")

#Ejercicio 3
def test_exercise_3():
    sum_by_rows, sum_by_columns, max_value, matrix = Exercises.exercise_3()

    print("\nEjercicio 3: \n" \
        "Matriz:\n" + str(matrix) + "\n" \
        "Suma por filas: " + str(sum_by_rows) + "\n" \
        "Suma por columnas: " + str(sum_by_columns) + "\n" \
        "Valor máximo: " + str(max_value)+"\n")

#Ejercicio 4
def test_exercise_4():
    a=list([1,2,3])
    b=list([4,5,6])

    result = Exercises.exercise_4(a,b)

    print("\nEjercicio 4: \n" \
        "Lista a:" + str(a) + "\n" \
        "Lista b:" + str(b) + "\n" \
        "Resultado de A + B:\n" + str(result)+"\n")

#Ejercicio 5
def test_exercise_5():
    values= list([1,4,9,16,25])
    
    sqrt_array, log_array, exp_array = Exercises.exercise_5(values)
    print("\nEjercicio 5: \n" \
        "Valores usados:" + str(values) + "\n" \
        "Raíz cuadrada: " + str(sqrt_array) + "\n" \
        "Logaritmo natural: " + str(log_array) + "\n" \
        "Exponencial: " + str(exp_array)+"\n")

#Ejercicio 6
def test_exercise_6():
    mean, std_dev, percentile_90, variance, random_numbers = Exercises.exercise_6()

    print("\nEjercicio 6: \n" \
        "Media: " + str(mean) + "\n" \
        "Desviación estándar: " + str(std_dev) + "\n" \
        "Percentil 90: " + str(percentile_90) + "\n" \
        "Varianza: " + str(variance)+"\n")

#Ejercicio 7
def test_exercise_7():
    greater_than_10, modified_array = Exercises.exercise_7()

    print("\nEjercicio 7: \n"\
        "Números mayores que 10: " + str(greater_than_10) + "\n"\
        "Array modificado (menores que 10 reemplazados por 0): " + str(modified_array)+"\n")

#Ejercicio 8
def test_exercise_8():
    determinant, inverse, eigenvalues, eigenvectors = Exercises.exercise_8()

    print("\nEjercicio 8: \n" \
        "Determinante: " + str(determinant) + "\n" \
        "Inversa:\n" + str(inverse) + "\n" \
        "Valores propios: " + str(eigenvalues) + "\n" \
        "Vectores propios:\n" + str(eigenvectors)+"\n")

#Ejercicio 9
def test_exercise_9():
    solution, Coeficents, eResults = Exercises.exercise_9()

    print("\nEjercicio 9: \n" \
        "Coeficientes de la ecuación: " + str(Coeficents) + "\n" \
        "Resultados de las ecuaciones: " + str(eResults)+"\n" \
        "Solución del sistema de ecuaciones: " + str(solution) + "\n" )

#Ejercicio 10
def test_exercise_10():
    elementwise_product, matrix_product, matrix_A, matrix_B = Exercises.exercise_10()

    print("\nEjercicio 10: \n" \
        "Matriz A:\n" + str(matrix_A) + "\n" \
        "Matriz B:\n" + str(matrix_B) + "\n" \
        "Producto elemento a elemento:\n" + str(elementwise_product) + "\n" \
        "Producto de matrices:\n" + str(matrix_product) + "\n")

def run_tests():
    test_exercise_1()
    print("//////////////////////////////////////////////") 
    test_exercise_2()
    print("//////////////////////////////////////////////") 
    test_exercise_3()
    print("//////////////////////////////////////////////") 
    test_exercise_4()
    print("//////////////////////////////////////////////") 
    test_exercise_5()
    print("//////////////////////////////////////////////") 
    test_exercise_6()
    print("//////////////////////////////////////////////") 
    test_exercise_7()
    print("//////////////////////////////////////////////") 
    test_exercise_8()
    print("//////////////////////////////////////////////")
    test_exercise_9()
    print("//////////////////////////////////////////////")
    test_exercise_10()
    print("//////////////////////////////////////////////")





run_tests()