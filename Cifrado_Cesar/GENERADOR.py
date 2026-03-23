import string
import random

ALFABETO = string.ascii_lowercase + string.digits

def cifrar_con_reto(texto, clave, direccion):
    texto_cifrado = ""
    desplazamiento = clave * direccion
    
    for caracter in texto.lower():
        if caracter not in ALFABETO:
            texto_cifrado += caracter
        else:
            indice = ALFABETO.index(caracter)
            nuevo_indice = (indice + desplazamiento) % len(ALFABETO)
            texto_cifrado += ALFABETO[nuevo_indice]
    return texto_cifrado

if __name__ == "__main__":
    mensaje = "El eclipse fu3 ay3r"
    clave_random = random.randint(1, len(ALFABETO) - 1)
    direccion_random = random.choice([1, -1])
    
    encriptado = cifrar_con_reto(mensaje, clave_random, direccion_random)
    
    print("--- Texto generado ---")
    print(f"Texto cifrado: {encriptado}")
    print("---------------------")
   
   #Guarda la solucion
    sentido = "derecha" if direccion_random == 1 else "izquierda"
    print(f"(Hey... La solución es la Clave: {clave_random}, Dirección: {sentido})")