import pytest
from Ejemplo_T3_Caso import validar_nota, estado_estudiante

# Esta primera prueba ayuda a saber si una nota dentro del rango establecido debe ser aceptada o no
def test_nota_valida():
    assert validar_nota(15) is True

# Esta segunda prueba permite saber si una nota está fuera del rango permitido (lanza un mensaje de error   )
def test_nota_invalida():
    with pytest.raises(ValueError):
        validar_nota(25)

# Esta tercera prueba verifica el estado del alumno según el promedio que sacó
def test_estado_estudiante():
    assert estado_estudiante(14) == "APROBADO"
    assert estado_estudiante(8) == "DESAPROBADO"