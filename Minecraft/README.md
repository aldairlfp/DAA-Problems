# MineCraft

## Problema

En el juego de MineCraft una de las principales distracciones es la
construccion, los mejores jugadores logran hacer monumentos imponentes que
sorprenden a todos. Actualmente se esta llevando a cabo un torneo de
construcción en el juego, donde la tarea es hacer un muro. Un muro es,
como sabemos, una ilera de columnas de bloques de piedra, todos de la misma
altura. En MineCraft, para llevar a cabo esta tarea hay 3 movimientos válidos:

- sacar un bloque de piedra del inventario y aumentar la altura de la columna
en cuestion en 1 de altura
- destruir un bloque de piedra de una columna y disminuir la altura de la
columna en cuestion en 1 de altura
- mover un bloque de piedra de una columna a otra, aumentando la altura de la
2da columna y disminuyendo la de la 1ra en 1 de altura cada una.

Se sabe que hacer cada movimiento consume c, d y m de energia respectivamente,
y que en los inventarios de los jugadores hay suficienues bloques de piedra
siempre. Los jugadores comienzan a jugar con un muro a medio hacer aleatorio,
osea, se les da una cantidad n de columnas de bloques de piedra en ilera, de
disímiles tamaños y el ganador del torneo será el que construya un muro de
largo n utilizando la menor cantidad de energia, no se permite crear columnas
nuevas ni dejar huecos de antiguas columnas en el muro porsupuesto.

Elabore una estrategia que asegure que para cualquier muro inicial a medio
hacer con que comience, usted logrará hacer el muro pedido utilizando la menor
cantidad de energia posible.

## Respuesta

### Fuerza bruta

La función `fuerza_bruta` itera sobre todas las alturas posibles desde la altura
mínima hasta la altura máxima.
Para cada altura, se llama a la función `costo_total` para calcular el costo de
energía asociado con esa altura.
La función `costo_total` tiene una complejidad temporal de O(n), ya que recorre
todas las columnas del muro para calcular los costos de agregar, quitar y mover
bloques.
Dado que hay (`altura_max` - `altura_min` + 1) alturas posibles y que para cada
altura, la función `costo_total` tiene una complejidad temporal de O(n), la
complejidad temporal total del enfoque de fuerza bruta es
O(n * (`altura_max` - `altura_min` + 1)).

$n$: número de columnas en el muro\
$h_i$: altura de la columna $i$, para $i$ = 1, 2, ..., n\
$H$: altura objetivo para todas las columnas\
$c$: costo de agregar un bloque\
$d$: costo de quitar un bloque\
$m$: costo de mover un bloque de una columna a otra\

Definiciones:

Costo total: La cantidad total de energía consumida para alcanzar la altura objetivo $H$ en todas las columnas.

Inicialmente, la altura óptima $H$ es desconocida. Para encontrarla, debemos examinar todas las posibles alturas de muro desde la altura mínima hasta la altura máxima.

Supongamos que hemos seleccionado una altura $H$ como candidata. Para calcular
el costo total asociado con esta altura, debemos considerar tres acciones: agregar, quitar y mover bloques. El objetivo es minimizar el costo total.

Para cada columna $i$ en el muro ($i$ = 1, 2, ..., n), comparamos la altura $h_i$ con la altura objetivo H:

- Si $h_i$ < $H$, necesitamos agregar ($H - $h_i$) bloques. El costo asociado es
$c$ * ($H$ - $h_i$).
- Si $h_i$ > $H$, necesitamos quitar ($h_i$ - $H$) bloques. El costo asociado es $d$ * ($h_i$ - $H$).
- Si $h_i$ = $H$, no se necesita ninguna acción y el costo asociado es 0.

Ahora, consideramos la acción de mover bloques. Si el costo de mover un bloque ($m$) es menor que la suma de los costos de agregar y quitar ($c$ + $d$), podemos reducir el costo total moviendo bloques de una columna a otra en lugar de agregar y quitar bloques:

- Calculamos el número total de bloques sobrantes y el número total de bloques faltantes.
- Si el costo de mover un bloque es menor que la suma de los costos de agregar y quitar, movemos la cantidad mínima de bloques entre las columnas sobrantes y las columnas faltantes. El costo asociado es $m$ * min(`bloques_sobrantes`, `bloques_faltantes`).
- Actualizamos el número de bloques sobrantes y faltantes después de mover los bloques.

Sumamos los costos asociados con cada acción (agregar, quitar y mover) para obtener el costo total asociado con la altura objetivo $H$.

Repetimos los pasos 2-5 para todas las posibles alturas objetivo $H$ desde la altura mínima hasta la altura máxima.

La altura óptima es la que tiene el costo total mínimo entre todas las alturas posibles.

La correctitud y optimalidad del algoritmo se garantizan porque se examinan todas las posibles alturas de muro y se calcula el costo total para cada altura de manera precisa, teniendo en cuenta todas las acciones posibles y sus costos asociados.

Al final del proceso, la altura óptima y el costo total mínimo encontrados corresponden a la solución óptima del problema.

Inicialización:

La función `fuerza_bruta` inicializa el costo mínimo como infinito (`float("inf")`) y la altura óptima como None. Estos valores sirven como base para comparar los costos calculados en las siguientes iteraciones.

Búsqueda exhaustiva:

El algoritmo de fuerza bruta examina todas las posibles alturas de muro desde la altura mínima hasta la altura máxima (ambas inclusive) y, en cada iteración, calcula el costo total utilizando la función `costo_total`. Dado que se prueban todas las posibles alturas, el algoritmo garantiza que encontrará la solución óptima.

Actualización del costo mínimo y la altura óptima:

En cada iteración, si el costo calculado es menor que el costo mínimo actual, se actualiza el costo mínimo y la altura óptima. Al final del bucle, la altura óptima almacenada corresponderá a la solución óptima del problema, y el costo mínimo almacenado será el costo total asociado a dicha solución óptima.

Correctitud:

La correctitud del algoritmo se basa en el hecho de que se examinan todas las posibles alturas de muro, garantizando que no se omita ninguna solución viable. Además, la función `costo_total` calcula de manera precisa la energía consumida para cada altura de muro, lo que permite comparar de manera correcta los costos asociados a cada solución.

Optimalidad:

La optimalidad del algoritmo se deriva de la correctitud del mismo. Dado que el algoritmo explora todas las posibles alturas de muro y actualiza el costo mínimo y la altura óptima de manera adecuada, se garantiza que la solución obtenida al final del proceso será la óptima.

En resumen, el algoritmo de fuerza bruta es correcto y óptimo porque explora exhaustivamente todas las posibles alturas de muro y utiliza la función `costo_total` para calcular y comparar los costos asociados a cada solución de manera precisa. Al final del proceso, la altura óptima y el costo mínimo almacenados corresponden a la solución óptima del problema.

Para realizar una demostración de las cotas superior (O) e inferior (Ω) del algoritmo de fuerza bruta para este problema, primero analicemos los pasos involucrados en el algoritmo de fuerza bruta y cuantifiquemos su complejidad temporal.

Pasos del algoritmo de fuerza bruta:

- Iterar sobre todas las posibles alturas objetivo $H$ desde la altura mínima hasta la altura máxima del muro.
- Para cada altura objetivo $H$, calcular el costo total necesario para transformar el muro en un muro de altura $H$.
- Comparar los costos totales de todas las alturas objetivo y seleccionar la altura que minimiza el costo total.

Ahora analicemos la complejidad temporal de cada paso:

La cantidad de posibles alturas objetivo $H$ es igual a (altura máxima - altura mínima + 1). Por lo tanto, la complejidad de este paso es O(altura máxima - altura mínima).

Para calcular el costo total necesario para transformar el muro en un muro de altura $H$, es necesario iterar sobre todas las columnas ($n$) y realizar operaciones de agregar, quitar o mover bloques. La complejidad de este paso es O($n$).

Comparar los costos totales de todas las alturas objetivo tiene una complejidad de O(altura máxima - altura mínima).

Entonces, la complejidad total del algoritmo de fuerza bruta es O((altura máxima - altura mínima) * $n$).

Para obtener la cota inferior (Ω), consideremos el caso en el que todas las columnas del muro tienen la misma altura y no se necesita realizar ninguna acción para transformar el muro. En este caso, el algoritmo de fuerza bruta todavía necesita verificar todas las posibles alturas objetivo $H$ y calcular el costo total para cada altura. Por lo tanto, la cota inferior es Ω((altura máxima - altura mínima) * $n$).

La cota superior (O) y la cota inferior (Ω) coinciden en este caso, lo que significa que el algoritmo de fuerza bruta tiene una complejidad temporal de Θ((altura máxima - altura mínima) * $n$).

## Busqueda ternaria

Correctitud y optimalidad:

La búsqueda ternaria es un algoritmo para encontrar el mínimo (o máximo) de una función unimodal. En este caso, la función de costo total es unimodal, ya que para alturas muy bajas o muy altas, el costo de energía será alto y habrá un mínimo local en algún punto intermedio.

La búsqueda ternaria evalúa dos puntos en el espacio de búsqueda ($m1$ y $m2$) y se actualizan los límites ($l$ y $r$) dependiendo de cuál de los dos puntos tiene un costo menor. Al repetir este proceso, el espacio de búsqueda se reduce hasta que se encuentra el mínimo aproximado.

La solución es óptima en términos de energía consumida, ya que la función de costo total considera todos los posibles movimientos (agregar, quitar y mover bloques) y sus respectivos costos. Además, la búsqueda ternaria garantiza que se encuentra la altura óptima que minimiza la energía consumida.

En resumen, la solución de búsqueda ternaria es correcta y óptima, ya que encuentra la altura que minimiza la energía consumida, teniendo en cuenta todos los posibles movimientos y sus costos asociados. La complejidad temporal del algoritmo es O(log(`altura_max` - `altura_min`)), lo que lo hace eficiente para encontrar la solución en un espacio de búsqueda reducido.

Claro, vamos a analizar la complejidad temporal del código proporcionado que combina la búsqueda ternaria y la función `costo_total` paso a paso.

Búsqueda ternaria:
La búsqueda ternaria tiene una complejidad temporal de O(log(`altura_max` - `altura_min`)). Esto se debe a que el algoritmo divide el espacio de búsqueda en tres partes iguales y descarta un tercio del intervalo en cada iteración. El proceso se repite hasta que el intervalo de búsqueda se reduce a un valor epsilon (`eps`), que en este caso es igual a 0.01 .

La función `costo_total` tiene una complejidad temporal de O(n), donde n es el número de columnas en el muro actual. Esto se debe a que la función itera una vez sobre todas las columnas del muro para calcular la energía consumida en función de la altura objetivo.

Función `costo_total`:(Igual que en Fuerza Bruta)
La función `costo_total` tiene una complejidad temporal de O(n), donde n es el número de columnas en el muro actual. Esto se debe a que la función itera una vez sobre todas las columnas del muro para calcular la energía consumida en función de la altura objetivo.

En el proceso de búsqueda ternaria, la función `costo_total` se llama en cada iteración para calcular la energía consumida para las dos alturas intermedias m1 y m2. Dado que la búsqueda ternaria tiene una complejidad temporal de O(log(`altura_max` - `altura_min`)), y la función `costo_total` se llama en cada iteración con una complejidad temporal de O(n), la complejidad total del algoritmo es el producto de estas dos complejidades:

Complejidad total = O(n) *O(log(`altura_max` - `altura_min`))
= O(n* log(`altura_max` - `altura_min`))

Entonces, la complejidad temporal del código proporcionado que combina la búsqueda ternaria y la función `costo_total` es O(n * log(`altura_max` - `altura_min`)).

Vamos a analizar el código proporcionado paso a paso y demostrar la correctitud y complejidad del algoritmo.

Primero, repasemos el código:

Se define la función `busqueda_ternaria(muro_actual, c, d, m, l, r, eps=0.01)` que realiza la búsqueda ternaria para encontrar la altura óptima.

Se define la función `costo_total(muro_actual, h, c, d, m)` que calcula la energía consumida para construir un muro de altura $h$ a partir del muro actual.

Se utiliza la función `busqueda_ternaria` para encontrar la altura óptima que minimiza la energía consumida.

Se redondea la altura óptima encontrada para asegurarse de que sea un valor entero.

Se calcula la energía consumida utilizando la función `costo_total` con la altura óptima encontrada.

Correctitud:

La función `costo_total` calcula correctamente la energía consumida para construir un muro de altura $h$, teniendo en cuenta los costos de agregar, quitar y mover bloques. La función garantiza que se utilice la menor cantidad de energía posible al comparar la energía consumida para mover bloques frente a agregar y quitar bloques.
La función `busqueda_ternaria` busca la altura óptima utilizando la función `costo_total`. Dado que la función de costo es unimodal en el rango de alturas, la búsqueda ternaria garantiza que se encuentre el mínimo global de la función de costo.

Complejidad temporal:

La función `costo_total` tiene una complejidad de O(n), donde n es el número de columnas en el muro actual, ya que se itera sobre todas las columnas del muro una vez.
La función `busqueda_ternaria` tiene una complejidad de O(log(`altura_max` - `altura_min`)) debido al proceso iterativo de reducción del espacio de búsqueda en cada iteración.
La complejidad temporal total del algoritmo es O(n * log(`altura_max` - `altura_min`)), ya que la función `costo_total` se llama en cada iteración de la búsqueda ternaria.

Optimalidad:

El algoritmo encuentra la altura óptima que minimiza la energía consumida, ya que utiliza la búsqueda ternaria en una función de costo unimodal para encontrar el mínimo global.
La función `costo_total` garantiza que se utilice la menor cantidad de energía posible al comparar la energía consumida para mover bloques frente a agregar y quitar bloques.
En resumen, el algoritmo proporcionado es correcto y óptimo, y tiene una complejidad temporal de O(n * log(`altura_max` - `altura_min`)).

La función de costo, tal como está definida actualmente, es discreta y no es fácilmente interpolable en reales. Sin embargo, podemos intentar construir una expresión analítica aproximada utilizando una función continua.

Para simplificar la función de costo, primero debemos eliminar las condiciones de mover bloques solo cuando el costo de mover sea menor que la suma de los costos de agregar y quitar bloques. En su lugar, asumamos que el costo de mover bloques es simplemente una combinación lineal de los costos de agregar y quitar bloques, con un peso $α$, donde $0 <= α <= 1$:

`costo_mover = α * (costo_agregar + costo_quitar)`

Entonces, podemos escribir una expresión analítica aproximada para la función de costo total como:

$costo(h) = A(h) *c + Q(h)* d + M(h) *(α* (c + d))$

Donde:

$h$ es la altura objetivo,
$A(h)$, $Q(h)$ y $M(h)$ son las cantidades de bloques agregados, quitados y movidos, respectivamente, como funciones de $h$,
$c$, $d$ y $α$ son los costos de agregar, quitar y mover bloques, respectivamente.

Una función unimodal es una función que primero es monótonamente creciente y luego monótonamente decreciente o viceversa. En otras palabras, hay un único punto de mínimo (o máximo) local en el dominio de la función.
Para demostrar que la función de costo es unimodal, consideremos el problema de construcción del muro en términos del costo de energía en función de la altura objetivo $h$. El objetivo es minimizar el costo total de energía al construir el muro con altura $h$. La función de costo total es la suma de tres componentes: energía para agregar bloques (`E_agregar`), energía para quitar bloques (`E_quitar`) y energía para mover bloques (`E_mover`). Cada uno de estos componentes puede ser calculado en función de la altura objetivo $h$ y el costo de cada operación ($c$ para agregar, $d$ para quitar y $m$ para mover). Observemos que `E_agregar` es una función monótonamente decreciente con respecto a $h$: a mayor altura, menos bloques necesitamos agregar y, por lo tanto, menos energía consumimos.
`E_quitar` es una función monótonamente creciente con respecto a $h$: a mayor altura, menos bloques necesitamos quitar y, por lo tanto, menos energía consumimos.
`E_mover` es una función no decreciente con respecto a $h$: a mayor altura, podemos mover más bloques (siempre que $m < c + d$), pero la energía consumida no aumentará. Cuando $m >= c + d$, no moveremos bloques, y la energía consumida será 0.
Dado que `E_agregar` es monótonamente decreciente y `E_quitar` es monótonamente creciente, la suma de estos dos componentes (`E_agregar + E_quitar`) es unimodal, ya que primero disminuye y luego aumenta. La función de costo total es la suma de `E_agregar`, `E_quitar` y `E_mover`. Como `E_mover` es no decreciente, la suma de las tres componentes también es unimodal. Por lo tanto, la función de costo total es unimodal con respecto a la altura objetivo $h$, y podemos aplicar la búsqueda ternaria para encontrar el mínimo.
