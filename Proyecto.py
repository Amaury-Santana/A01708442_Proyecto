# Entradas
edad = int(input("Ingrese su edad: "))
genero_favorito = input("Ingrese su género favorito: ")
duracion_estimadapref = int(input("Ingrese la duración estimada preferida (en minutos): "))
tematica_favorita = input("Ingrese su temática favorita: ")

# Lista de películas con 10 películas de diferentes plataformas y características organizada como una matriz 
lista_peliculas = [
    ["Película 1", 13, "Acción", 120, "Aventura", "Netflix"],
    ["Película 2", 18, "Drama", 150, "Historia", "Amazon Prime"],
    ["Película 3", 7, "Comedia", 90, "Familia", "Disney+"],
    ["Película 4", 16, "Terror", 100, "Suspenso", "HBO Max"],
    # Más películas...
]

# Función para calcular el bono adicional
def calcular_bono(pelicula, genero_favorito):
    bono = 0
    if pelicula[2].lower() == genero_favorito.lower():  # género es el tercer elemento
        bono = 10  # Bono adicional por coincidencia exacta de género
    return bono

# Función para calcular similitud
def calcular_similitud(pelicula, edad, genero_favorito, duracion_estimadapref, tematica_favorita):
    similitud = 0
    
    # Similitud basada en la edad
    if pelicula[1] <= edad:  #edad mínima es el segundo elemento
        similitud += 25
    
    # Similitud basada en el género
    if pelicula[2].lower() == genero_favorito.lower():  #género es el tercer elemento
        similitud += 25
    
    # Similitud basada en la duración
    if abs(pelicula[3] - duracion_estimadapref) <= 15:  #duración es el cuarto elemento
        similitud += 25
    
    # Similitud basada en la temática
    if pelicula[4].lower() == tematica_favorita.lower():  #temática es el quinto elemento
        similitud += 25
    
    return similitud

# Proceso de recomendación
def procesar_recomendaciones(lista_peliculas, edad, genero_favorito, duracion_estimadapref, tematica_favorita, umbral_similitud, margen_duracion):
    lista_de_recomendaciones = []
    for pelicula in lista_peliculas:
        # Calcular similitud base
        similitud = calcular_similitud(pelicula, edad, genero_favorito, duracion_estimadapref, tematica_favorita)
        
        # Agregar el bono adicional por coincidencia exacta en el género
        similitud += calcular_bono(pelicula, genero_favorito)
        
        # Ajustar la similitud si la duración está dentro del margen permitido
        if abs(pelicula[3] - duracion_estimadapref) <= margen_duracion:
            similitud += 25
        
        if similitud >= umbral_similitud:
            lista_de_recomendaciones.append({"titulo": pelicula[0], "plataforma": pelicula[5], "similitud": similitud})
    
    return lista_de_recomendaciones

# Parámetros para ajustar el umbral de similitud y margen de duración
umbral_similitud = 75
margen_duracion = 15

# Ciclo para ajustar los criterios hasta obtener recomendaciones
lista_de_recomendaciones = []

while len(lista_de_recomendaciones) == 0:
    lista_de_recomendaciones = procesar_recomendaciones(lista_peliculas, edad, genero_favorito, duracion_estimadapref, tematica_favorita, umbral_similitud, margen_duracion)
    
    if len(lista_de_recomendaciones) == 0:
        print("No se encontraron recomendaciones, ajustando criterios...")
        
        # Ajustar los criterios
        umbral_similitud -= 25
        margen_duracion += 15
        
        if umbral_similitud < 25:
            print("No se encontraron recomendaciones con los criterios actuales.")
            break

# Mostrar las recomendaciones
    """
    Aqui voy a poner como voy a mostrar y ordenar las recomendaciones, cosa que todavía no se hacer
    """





 

