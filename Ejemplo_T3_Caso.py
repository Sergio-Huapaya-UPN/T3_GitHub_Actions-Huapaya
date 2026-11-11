# Permite validar que la nota esté en el rango permitido (0 a 20)
def validar_nota(nota):
    if not 0 <= nota <= 20:
        raise ValueError("La nota debe estar entre 0 y 20")
    return True

# Permite saber si el estudiante aprueba o desaprueba según su promedio
def estado_estudiante(promedio):
    validar_nota(promedio)
    return "APROBADO" if promedio >= 10.5 else "DESAPROBADO"