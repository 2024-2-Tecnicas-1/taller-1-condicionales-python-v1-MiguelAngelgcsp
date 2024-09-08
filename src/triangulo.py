def evaluar(a, b, c):
    # Verifica si los lados forman un triángulo válido
    if a + b <= c or a + c <= b or b + c <= a:
        return "No es un triángulo válido"
    
    # Verifica si el triángulo es equilátero
    if a == b and b == c:
        return "El triángulo es equilátero"
    
    # Verifica si el triángulo es isósceles
    elif a == b or a == c or b == c:
        return "El triángulo es isósceles"
    
    # Si no es equilátero ni isósceles, es escaleno
    else:
        return "El triángulo es escaleno"
if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
