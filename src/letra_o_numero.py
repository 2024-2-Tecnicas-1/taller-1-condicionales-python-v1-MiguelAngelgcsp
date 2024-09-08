def evaluar(caracter):
 
    codigo_ascii = ord(caracter)
    
   
    if '0' <= caracter <= '9':
        return "Es número"
    
    
    if 'A' <= caracter <= 'Z':
        return "Es letra mayúscula"
    
  
    if 'a' <= caracter <= 'z':
        return "Es letra minúscula"
    
   
    return "No es letra ni número"

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
