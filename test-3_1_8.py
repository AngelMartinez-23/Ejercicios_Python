# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

# Función que verifica si una palabra es un palíndromo
def es_palindromo(palabra):
    # Normalizamos la palabra: quitamos espacios y la ponemos en minúsculas
    palabra_limpia = ''.join(filter(str.isalnum, palabra)).lower()
    return palabra_limpia == palabra_limpia[::-1]

# Función para ejecutar los tests manualmente
def ejecutar_tests():
    # 1. Test palíndromo simple
    print("Test 1 - Palíndromo simple (radar):", "OK" if es_palindromo("radar") else "FALLÓ")
    
    # 2. Test no es un palíndromo
    print("Test 2 - No palíndromo (palabra):", "OK" if not es_palindromo("palabra") else "FALLÓ")
    
    # 3. Test mayúsculas y minúsculas
    print("Test 3 - Mayúsculas y minúsculas (Radar):", "OK" if es_palindromo("Radar") else "FALLÓ")
    
    # 4. Test palíndromo con espacios y caracteres
    print("Test 4 - Palíndromo con espacios (anita lava la tina):", "OK" if es_palindromo("anita lava la tina") else "FALLÓ")
    
    # 5. Test cadena vacía
    print("Test 5 - Cadena vacía:", "OK" if es_palindromo("") else "FALLÓ")

# Ejecutar los tests
ejecutar_tests()

