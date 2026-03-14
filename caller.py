

# FREEZE CODE BEGIN
x = int(input())
y = float(input())
def promedio_estudiante(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones de estudiantes.
 
    Args:
        calificaciones: lista de números que representan las calificaciones.
 
    Returns:
        float: la media aritmética de las calificaciones,
               o 0.0 si la lista está vacía.
    """
    if len(calificaciones) == 0:
        return 0.0
 
    return float(sum(calificaciones) / len(calificaciones))

