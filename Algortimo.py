Algortimo proyecto
Entradas
Edad (número entero)
Género_favorito (texto | string) 
Duración_estimadapref (número entero)
Temática_favorita (texto | string) 

Proceso:
1.Pedir Edad
2.Pedir Género_favorito
3.Pedir Duración_estimadapref
4.Pedir Temática_favorita
5.Inicializar Lista_películas con 10 películas de las plataformas Netflix, Amazon Prime, Disney+ y Max de diferentes características.
6.Inicializar Lista_de_recomendaciones = ()
7.Para cada película en Lista_películas:
7.1 Calcular similitud según Edad:
7.1.1 Si Edad está dentro del rango permitido para la película, asignar 25% de similitud.
7.2 Calcular similitud según Género_favorito:
7.2.1 Si Género de la película = Género_favorito, asignar 25% de similitud.
7.3 Calcular similitud según Duración_estimadapref:
7.3.1 Si Duración de la película está dentro del rango de Duración_estimadapref ± 15 minutos, asignar 25% de similitud.
7.4 Calcular similitud según Temática_favorita:
7.4.1 Si Temática de la película = Temática_favorita, asignar 25% de similitud.
7.5 Sumar las similitudes calculadas para obtener el Porcentaje_de_similitud.
7.6 Si Porcentaje_de_similitud >= 75%, Agregar película a Lista_de_recomendaciones con su Porcentaje_de_similitud.
8 Si Lista_de_recomendaciones no está vacía:
8.1 Ordenar Lista_de_recomendaciones por Porcentaje_de_similitud de mayor a menor.
8.2 Mostrar las 3 primeras recomendaciones que son las que tienen mayor porcentaje de similitud al usuario y su plataforma.
9.Si no hay resultados en Lista_de_recomendaciones:
9.1 Ampliar el rango de Duración_estimadapref ± 30 minutos
9.2 Ampliar rango de Porcentaje_de_similitud >= 50%  
9.3 Regresar desde paso 7
10.Si todavía no hay resultados regresar al Paso 1 y pedir inputs distintos. 

Salidas:
Lista_de_recomendaciones (texto | string) con las 3 películas recomendadas. 
