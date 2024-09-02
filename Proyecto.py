# Entradas
edad = int(input("Ingrese su edad: "))
genero_favorito = input("Ingrese su género favorito: ")
duracion_estimadapref = int(input("Ingrese la duración estimada preferida (en minutos): "))
tematica_favorita = input("Ingrese su temática favorita: ")

# Inicializar lista de películas con 10 películas de diferentes plataformas y características
lista_peliculas = [
    {"titulo": "Película 1", "edad_minima": 13, "genero": "Acción", "duracion": 120, "tematica": "Aventura", "plataforma": "Netflix"},
    {"titulo": "Película 2", "edad_minima": 18, "genero": "Drama", "duracion": 150, "tematica": "Historia", "plataforma": "Amazon Prime"},
    # Agregar más películas con diferentes características...
]

# Inicializar lista de recomendaciones
lista_de_recomendaciones = []

# Función para calcular similitud
def calcular_similitud(pelicula, edad, genero_favorito, duracion_estimadapref, tematica_favorita):
    similitud_edad = 0
    similitud_genero = 0
    similitud_duracion = 0
    similitud_tematica = 0

    # Calcular similitud Edad
    if pelicula["edad_minima"] <= edad:
        similitud_edad = 25

    # Calcular similitud Género_favorito
    if pelicula["genero"].lower() == genero_favorito.lower():
        similitud_genero = 25
    
    # Calcular similitud Duración_estimadapref
    if abs(pelicula["duracion"] - duracion_estimadapref) <= 15:
        similitud_duracion = 25
    
    # Calcular similitud Temática_favorita
    if pelicula["tematica"].lower() == tematica_favorita.lower():
        similitud_tematica = 25

    # Calcular bono adicional
    bono = calcular_bono(pelicula, genero_favorito)

    # Calcular el porcentaje de similitud
    porcentaje_de_similitud = similitud_edad + similitud_genero + similitud_duracion + similitud_tematica + bono

    return porcentaje_de_similitud

# Función para calcular el bono adicional
def calcular_bono(pelicula, genero_favorito):
    bono = 0
    if pelicula["genero"].lower() == genero_favorito.lower():
        bono = 10  # Bono adicional de similitud
    return bono

# Proceso de cálculo de similitud
def procesar_recomendaciones(lista_peliculas, edad, genero_favorito, duracion_estimadapref, tematica_favorita, umbral_similitud, margen_duracion):
    lista_de_recomendaciones = []
    for pelicula in lista_peliculas:
        porcentaje_de_similitud = calcular_similitud(pelicula, edad, genero_favorito, duracion_estimadapref, tematica_favorita)
        
        # Ajustar similitud de duración según el margen proporcionado
        if abs(pelicula["duracion"] - duracion_estimadapref) <= margen_duracion:
            porcentaje_de_similitud += 25
        
        if porcentaje_de_similitud >= umbral_similitud:
            lista_de_recomendaciones.append({"titulo": pelicula["titulo"], "plataforma": pelicula["plataforma"], "similitud": porcentaje_de_similitud})

    return lista_de_recomendaciones

# Aplicar el cálculo de similitud inicial
lista_de_recomendaciones = procesar_recomendaciones(lista_peliculas, edad, genero_favorito, duracion_estimadapref, tematica_favorita, 75, 15)

# Mostrar y ordenar las recomendaciones
if lista_de_recomendaciones:
    """
    Aqui voy a poner como voy a mostrar y ordenar las recomendaciones, cosa que todavía no se hacer
    """
else:
    # Modificar criterios en caso de no encontrar recomendaciones suficientes
    print("No se encontraron suficientes recomendaciones, modificando criterios...")
    
    # Refinar el proceso de recomendación con criterios más amplios
    lista_de_recomendaciones = procesar_recomendaciones(lista_peliculas, edad, genero_favorito, duracion_estimadapref, tematica_favorita, 50, 30)
    """
    Por lo que tengo entendido, al usar la función de def procesar_recoemndaciones ...  puedo ahorrarme poner todo de nuevo, entonces la línea de arriba solo cambia los dos valores que modifico 
    y hace que el código sea menos voltoso. 
    """
    if lista_de_recomendaciones:
        """
        Aqui voy a poner como voy a mostrar y ordenar las recomendaciones, cosa que todavía no se hacer
        """
    else:
        print("No se encontraron recomendaciones. Por favor, intente con diferentes entradas.")
