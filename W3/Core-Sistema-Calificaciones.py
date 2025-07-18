def obtener_numero_estudiantes():
    # Pide al usuario el número de estudiantes y devuelve el valor
    while True:
        try:
            num_estudiantes = int(input("Ingrese el número de estudiantes: "))
            if num_estudiantes < 0:
                print("El número de estudiantes no puede ser negativo. Inténtelo de nuevo.")
                continue
            return num_estudiantes
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def obtener_nombre_estudiante():
    # Pide al usuario el nombre del estudiante y devuelve el valor
    while True:
        nombre = input("Ingrese el nombre del estudiante: ").strip()
        if nombre:
            return nombre
        else:
            print("El nombre del estudiante no puede estar vacío. Inténtelo de nuevo.")

def obtener_numero_asignaturas():
    # Pide al usuario el número de asignaturas y devuelve el valor
    while True:
        try:
            num_asignaturas = int(input("Ingrese el número de asignaturas para este estudiante: "))
            if num_asignaturas < 0:
                print("El número de asignaturas no puede ser negativo. Inténtelo de nuevo.")
                continue
            return num_asignaturas
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

def obtener_calificaciones(num_asignaturas):
    # Pide al usuario las calificaciones para cada asignatura y las devuelve en una lista
    calificaciones = []
    for i in range(num_asignaturas):
        nombre_asignatura = input(f"Ingrese el nombre de la asignatura {i+1}: ").strip()
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación para {nombre_asignatura} (0-10): "))
                if 0 <= calificacion <= 10:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("Calificación fuera del rango (0-10). Inténtelo de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un valor numérico para la calificación.")
    return calificaciones

def calcular_promedio(calificaciones):
    # Calcula y devuelve el promedio de las calificaciones
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(promedio):
    # Determina si el estudiante ha aprobado o reprobado basándose en el promedio
    return "Aprobado" if promedio >= 6.0 else "Reprobado"

def imprimir_resumen(estudiantes):
    # Imprime un resumen con el nombre de los estudiantes, su promedio y su estado
    print("\n--- Resumen de Calificaciones ---")
    if not estudiantes:
        print("No se ingresaron datos de estudiantes.")
        return
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}, Promedio: {estudiante['promedio']:.2f}, Estado: {estudiante['estado']}")
    print("---------------------------------")

num_estudiantes = obtener_numero_estudiantes()
estudiantes = []

for _ in range(num_estudiantes):
    nombre = obtener_nombre_estudiante()
    num_asignaturas = obtener_numero_asignaturas()
    calificaciones = obtener_calificaciones(num_asignaturas)
    promedio = calcular_promedio(calificaciones)
    estado = determinar_estado(promedio)
    
    estudiantes.append({
        'nombre': nombre,
        'promedio': promedio,
        'estado': estado
    })

imprimir_resumen(estudiantes)
