# Escribir un programa que pida al usuario una palabra y 
# muestre por pantalla el número de veces que contiene cada vocal.

# Función que cuenta las vocales en una palabra
def contar_vocales(palabra):
    vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    # Convertimos todo a minúsculas para que sea case-insensitive
    for letra in palabra.lower():
        if letra in vocales:
            vocales[letra] += 1
    return vocales

# Función para ejecutar los tests manualmente
def ejecutar_tests():
    # 1. Test con todas las vocales
    print("Test 1 - Todas las vocales (murcielago):", "OK" if contar_vocales("murcielago") == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1} else "FALLÓ")
    
    # 2. Test sin vocales
    print("Test 2 - Sin vocales (rhythm):", "OK" if contar_vocales("rhythm") == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0} else "FALLÓ")
    
    # 3. Test con una vocal repetida
    print("Test 3 - Una vocal repetida (eeee):", "OK" if contar_vocales("eeee") == {'a': 0, 'e': 4, 'i': 0, 'o': 0, 'u': 0} else "FALLÓ")
    
    # 4. Test con mayúsculas y minúsculas
    print("Test 4 - Mayúsculas y minúsculas (AeIoU):", "OK" if contar_vocales("AeIoU") == {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1} else "FALLÓ")
    
    # 5. Test cadena vacía
    print("Test 5 - Cadena vacía:", "OK" if contar_vocales("") == {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0} else "FALLÓ")

# Ejecutar los tests
ejecutar_tests()
