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

# Proceso de similitud
for pelicula in lista_peliculas:
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
        #.lower ayuda a garantintar que cuando se comparen variables no importen las mayúsculas o minúsculas
     
    # Calcular similitud Duración_estimadapref
    if abs(pelicula["duracion"] - duracion_estimadapref) <= 15:
        similitud_duracion = 25
        #abs sirve para que el número que devuelva sea entero (osea positivo)
    
    # Calcular similitud Temática_favorita
    if pelicula["tematica"].lower() == tematica_favorita.lower():
        similitud_tematica = 25


    """
    # Aplicar bono adicional si el género favorito coincide perfectamente
    bono = 0
    if pelicula["genero"].lower() == genero_favorito.lower():
        bono = 10  # Bono adicional de similitud
    """

    # Calcular el porcentaje de similitud   (operación de suma)
    porcentaje_de_similitud = similitud_edad + similitud_genero + similitud_duracion + similitud_tematica  #Aqui se tendría que agregar el bono
    
    # Agregar a la lista de recomendaciones si cumple el porcentaje solicitado de similitud
    if porcentaje_de_similitud >= 75:
        lista_de_recomendaciones.append({"titulo": pelicula["titulo"], "plataforma": pelicula["plataforma"], "similitud": porcentaje_de_similitud})
        #.append sirve para hacer una lista que cumplen con los criterios de similitud y los va agregando uno por uno


# Mostrar y ordenar las recomendaciones
if lista_de_recomendaciones:
    """
    Aqui voy a poner como voy a mostrar y ordenar las recomendaciones, cosa que todavía no se hacer
    """
else:
    # Modificar criterios en caso de no encontrar recomendaciones suficientes
    print("No se encontraron suficientes recomendaciones, modificando criterios...")

    # Ampliar el rango de duración y porcentaje de similitud
    lista_de_recomendaciones = []
    for pelicula in lista_peliculas:
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
        
        # Calcular similitud Duración_estimadapref con un rango más amplio
        if abs(pelicula["duracion"] - duracion_estimadapref) <= 30:
            similitud_duracion = 25
        
        # Calcular similitud Temática_favorita
        if pelicula["tematica"].lower() == tematica_favorita.lower():
            similitud_tematica = 25

        """
        # Aplicar bono adicional si el género favorito coincide perfectamente
        bono = 0
        if pelicula["genero"].lower() == genero_favorito.lower():
        bono = 10  # Bono adicional de similitud
        """
        
        # Calcular el porcentaje de similitud (operación de suma)
        porcentaje_de_similitud = similitud_edad + similitud_genero + similitud_duracion + similitud_tematica  #Aqui se tendría que agregar el bono
        
        # Agregar a la lista de recomendaciones si cumple el umbral de similitud más bajo
        if porcentaje_de_similitud >= 50:
            lista_de_recomendaciones.append({"titulo": pelicula["titulo"], "plataforma": pelicula["plataforma"], "similitud": porcentaje_de_similitud})
    
    # Mostrar y ordenar las nuevas recomendaciones
    if lista_de_recomendaciones:
        """
        Aqui voy a poner como voy a mostrar y ordenar las recomendaciones, cosa que todavía no se hacer
        """
    else:
        print("No se encontraron recomendaciones. Por favor, intente con diferentes entradas.")