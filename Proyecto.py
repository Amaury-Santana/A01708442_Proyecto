# Entradas
edad = int(input("Ingrese su edad: "))
genero_favorito = input("Ingrese su género favorito: ")
duracion_estimadapref = int(input("Ingrese la duración estimada preferida (en minutos): "))
tematica_favorita = input("Ingrese su temática favorita: ")

# Inicializar lista de películas con 10 películas de diferentes plataformas y características (Agregue un poco de más ejemplos)
lista_peliculas = [
    {"titulo": "Película 1", "edad_minima": 13, "genero": "Acción", "duracion": 120, "tematica": "Aventura", "plataforma": "Netflix"},
    {"titulo": "Película 2", "edad_minima": 18, "genero": "Drama", "duracion": 150, "tematica": "Historia", "plataforma": "Amazon Prime"},
    {"titulo": "Película 3", "edad_minima": 7, "genero": "Comedia", "duracion": 90, "tematica": "Familia", "plataforma": "Disney+"},
    {"titulo": "Película 4", "edad_minima": 16, "genero": "Terror", "duracion": 100, "tematica": "Suspenso", "plataforma": "HBO Max"},
    # Agregar más películas con diferentes características...
]

# Función para calcular el bono adicional
def calcular_bono(pelicula, genero_favorito):
    bono = 0
    if pelicula["genero"].lower() == genero_favorito.lower():
        bono = 10  # Bono adicional por coincidencia exacta de género
    return bono

# Función para calcular similitud
def calcular_similitud(pelicula, edad, genero_favorito, duracion_estimadapref, tematica_favorita):
    similitud = 0
    
    # Similitud basada en la edad
    if pelicula["edad_minima"] <= edad:
        similitud += 25
    
    # Similitud basada en el género
    if pelicula["genero"].lower() == genero_favorito.lower():
        similitud += 25
    
    # Similitud basada en la duración
    if abs(pelicula["duracion"] - duracion_estimadapref) <= 15:
        similitud += 25
    
    # Similitud basada en la temática
    if pelicula["tematica"].lower() == tematica_favorita.lower():
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
        if abs(pelicula["duracion"] - duracion_estimadapref) <= margen_duracion:
            similitud += 25
        
        if similitud >= umbral_similitud:
            lista_de_recomendaciones.append({"titulo": pelicula["titulo"], "plataforma": pelicula["plataforma"], "similitud": similitud})
    
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
# Uso el ciclo while para cambiar lo que antes hacía con def procesar recomendaciones_, no se si haga el código más eficiente pero fue de las pocas maneras que encontre para hacerlo. 


# Mostrar las recomendaciones
    """
    Aqui voy a poner como voy a mostrar y ordenar las recomendaciones, cosa que todavía no se hacer
    """





 

