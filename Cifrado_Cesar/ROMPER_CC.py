import string
from langdetect import detect, detect_langs

ALFABETO = string.ascii_lowercase

def algoritmo_descifrado(texto_cifrado, clave, direccion):
    texto_plano = ""
    desplazamiento = clave * direccion
    for caracter in texto_cifrado:
        if caracter not in ALFABETO:
            texto_plano += caracter
        else:
            indice = ALFABETO.index(caracter)
            nuevo_indice = (indice - desplazamiento) % len(ALFABETO)
            texto_plano += ALFABETO[nuevo_indice]
    return texto_plano

def fuerza_bruta_mejorada(texto_cifrado):
    espacio_claves = range(len(ALFABETO))
    posibles_resultados = []

    print("Analizando combinaciones...")

    for direccion in [1, -1]:
        for clave in espacio_claves:
            texto_plano = algoritmo_descifrado(texto_cifrado, clave, direccion)
            
            try:
                # Obtenemos la probabilidad de que sea español
                predicciones = detect_langs(texto_plano)
                for prob in predicciones:
                    if prob.lang == "es":
                        posibles_resultados.append({
                            'texto': texto_plano,
                            'clave': clave,
                            'dir': "derecha" if direccion == 1 else "izquierda",
                            'confianza': prob.prob
                        })
            except:
                continue
    posibles_resultados.sort(key=lambda x: x['confianza'], reverse=True)

    if posibles_resultados:
        print(f"\nSe encontraron {len(posibles_resultados)} posibles coincidencias:")
        for res in posibles_resultados[:3]:
            print(f"--- Confianza: {res['confianza']:.2%} ---")
            print(f"Texto: {res['texto']}")
            print(f"Clave: {res['clave']} | Dirección: {res['dir']}\n")
    else:
        print("No se encontró una combinación clara en español.")

if __name__ == "__main__":
    texto_cifrado = input("Introduce el texto cifrado: ").lower()
    fuerza_bruta_mejorada(texto_cifrado)