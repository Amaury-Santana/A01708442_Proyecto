# Opciones disponibles para el usuario
generos_disponibles = ["Acción", "Drama", "Comedia", "Terror"]
tematicas_disponibles = ["Aventura", "Historia", "Familia", "Suspenso"]

# Entradas con instrucciones para guiar al usuario
edad = int(input("Ingrese la edad mínima: "))
print(f"Géneros disponibles: {generos_disponibles}")
genero_favorito = input("Ingrese su género favorito (entre los disponibles): ")
while genero_favorito not in generos_disponibles:
    print("Por favor, elija un género válido.")
    genero_favorito = input(f"Ingrese su género favorito (entre {generos_disponibles}): ")

duracion_estimadapref = int(input("Ingrese la duración estimada preferida (en minutos): "))
print(f"Temáticas disponibles: {tematicas_disponibles}")
tematica_favorita = input("Ingrese su temática favorita (entre las disponibles): ")
while tematica_favorita not in tematicas_disponibles:
    print("Por favor, elija una temática válida.")
    tematica_favorita = input(f"Ingrese su temática favorita (entre {tematicas_disponibles}): ")

# Lista de 15 películas con diferentes plataformas y características organizada como una matriz 
lista_peliculas = [
    ["John Wick", 16, "Acción", 101, "Aventura", "Netflix"],
    ["El Padrino", 18, "Drama", 175, "Historia", "Amazon Prime"],
    ["Toy Story", 0, "Comedia", 81, "Familia", "Disney+"],
    ["El Conjuro", 16, "Terror", 112, "Suspenso", "HBO Max"],
    ["Mad Max: Fury Road", 15, "Acción", 120, "Aventura", "Netflix"],
    ["Titanic", 13, "Drama", 195, "Historia", "Amazon Prime"],
    ["Coco", 0, "Comedia", 105, "Familia", "Disney+"],
    ["It", 18, "Terror", 135, "Suspenso", "HBO Max"],
    ["Gladiador", 15, "Acción", 155, "Aventura", "Netflix"],
    ["El discurso del rey", 13, "Drama", 118, "Historia", "Amazon Prime"],
    ["Soul", 0, "Comedia", 100, "Familia", "Disney+"],
    ["La monja", 16, "Terror", 96, "Suspenso", "HBO Max"],
    ["Los Increíbles", 7, "Acción", 115, "Familia", "Disney+"],
    ["The Dark Knight", 15, "Acción", 152, "Aventura", "Netflix"],
    ["Forrest Gump", 13, "Drama", 142, "Historia", "Amazon Prime"],
    ["Monsters, Inc.", 7, "Comedia", 92, "Familia", "Disney+"],
    ["Jurassic Park", 12, "Acción", 127, "Aventura", "Netflix"],
]

# Función  para calcular similitud 
def calcular_similitud(pelicula, edad, genero_favorito, duracion_estimadapref, tematica_favorita):
    similitud = 0
    
    # Similitud basada en la edad
    if pelicula[1] <= edad:  # edad mínima es el segundo elemento
        similitud += 25
    
    # Similitud basada en el género (solo si coincide)
    if pelicula[2].lower() == genero_favorito.lower():  # género es el tercer elemento
        similitud += 25  
    else:
        return 0  # Si no coincide en género, no se considera la película
    
    # Similitud basada en la duración
    if abs(pelicula[3] - duracion_estimadapref) <= 15:  # duración es el cuarto elemento
        similitud += 25
    
    # Similitud basada en la temática (solo si coincide)
    if pelicula[4].lower() == tematica_favorita.lower():  # temática es el quinto elemento
        similitud += 25
    else:
        return 0  # Si no coincide en temática, no se considera la película
    
    return similitud

# Proceso de recomendación con ajuste para evitar duplicidad de puntos
def procesar_recomendaciones(lista_peliculas, edad, genero_favorito, duracion_estimadapref, tematica_favorita, umbral_similitud, margen_duracion):
    lista_de_recomendaciones = []
    for pelicula in lista_peliculas:
        # Calcular similitud base
        similitud = calcular_similitud(pelicula, edad, genero_favorito, duracion_estimadapref, tematica_favorita)
        
    
        
        # Ajustar la similitud si la duración está dentro del margen permitido 
        if abs(pelicula[3] - duracion_estimadapref) <= margen_duracion:
            pass  

        if similitud >= umbral_similitud:
            lista_de_recomendaciones.append({"titulo": pelicula[0], "plataforma": pelicula[5], "similitud": similitud})
    
    return lista_de_recomendaciones


# Parámetros para ajustar el umbral de similitud y margen de duración
umbral_similitud = 75
margen_duracion = 25

# Ciclo para ajustar los criterios hasta obtener recomendaciones
lista_de_recomendaciones = []

while len(lista_de_recomendaciones) == 0:
    lista_de_recomendaciones = procesar_recomendaciones(lista_peliculas, edad, genero_favorito, duracion_estimadapref, tematica_favorita, umbral_similitud, margen_duracion)
    
    if len(lista_de_recomendaciones) == 0:
        print("No se encontraron recomendaciones, ajustando criterios...")
        
        # Ajustar los criterios
        umbral_similitud -= 25
        margen_duracion += 25
        
        if umbral_similitud < 25:
            print("No se encontraron recomendaciones con los criterios propuestos, introduzca nuevos criterios.")
            break

# Mostrar las recomendaciones
if len(lista_de_recomendaciones) > 0:
    lista_de_recomendaciones = sorted(lista_de_recomendaciones, key=lambda x: x["similitud"], reverse=True)
    print("\nRecomendaciones encontradas:")
    for recomendacion in lista_de_recomendaciones:
        print(f"Título: {recomendacion['titulo']} | Plataforma: {recomendacion['plataforma']} | Similitud: {recomendacion['similitud']}%")

