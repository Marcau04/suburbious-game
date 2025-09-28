import random                  


class Secuencia:                                                                                                                                            #Introduccion de la clase secuencia, que es aquella la cual contiene todos los métodos que alterarán o tendrán que ver con la secuencia de los elementos del juego
    def __init__(self):                                                                                                                                     #introducimos las listas que serán indispensables para el desarrollo de el resto de los métodos de las clase secuencia
        self.sec = []                                                                                                                                       #lista que usaremos para generar una secuencia aleatoria en caso de que no tengamos una establecida
        for i in range(0, 30):
            self.sec.append('a')
        for i in range(5):
            self.sec.append('b')
        for i in range(1):
            self.sec.append('c')
        for i in range(6):
            self.sec.append('1')
        for i in range(1):
            self.sec.append('W')
        return None

    def crearSecuencia(self, secname, turno):                                                                                                               #En este método utilizaremos la lista creada anteriormente para establecer una secuencia aleatoria
        alca = 0
        new = ''
        secu = ""
        num = random.randrange(0, 42)                                                                                                                       #Generamos un número aleatorio que será el que determinara la posicion de la lista con el elemento que queremos "generar"
        if turno > 11:                                                                                                                                      #En caso de que la secuencia acabe, el método reiniciará la secuencia
            alca = turno // 11
            turno = turno - 11 * alca
        try:                                                                                                                                                #El método introduce una secuencia predeterminada extraida de un fichero externo
            f = open(f"{secname}", "r")
            fila = f.readlines()
            secu = fila[0]
            new = secu[turno - 1]
        except Exception:                                                                                                                                   #Si no existe fichero externo, generará una secuencia aleatoria
            new = self.sec[num]
        return new


class Tablero:                                                                                                                                              #Introduccion de la clase tablero, que es aquella la cual contiene todos los métodos que alterarán o tendrán que ver con el tablero del juego
    def __init__(self):                                                                                                                                     #Contiene las listas y variables que nos serán necesarias para el resto de metodos
        self.fil = 6
        self.col = 6
        self.matriz = []
        self.lista = []
        self.age = 0
        self.edadbigfoot = {}
        for i in range(0, 45):
            self.lista.append('.')
        for i in range(18):
            self.lista.append('a')
        for i in range(4):
            self.lista.append('b')
        for i in range(3):
            self.lista.append('c')
        for i in range(2):
            self.lista.append('1')
        # return None

    def crearTablero(self):                                                                                                                                 #Este método crea un tablero de manera aleatoria en caso de que no se introduzca uno predeterminado
        for i in range(self.fil):
            dato = ''
            fila = [dato] * self.col
            self.matriz.append(fila)
        return None

    def copiarTablero(self):                                                                                                                                #Este método copia un tablero introducido a través de un fichero
        f = open("test.tab.text", "r")
        fila = f.readlines()
        for i in range(self.fil):
            palabra = fila[i]
            for j in range(self.col):
                self.matriz[i][j] = palabra[j]

    def llenarTablero(self):                                                                                                                                #rellena el tablero con los elementos o bien extraidos del fichero o bien generados aleatoriamente

        num = 0

        for i in range(self.fil):
            for j in range(self.col):
                num = random.randrange(0, 71)
                self.matriz[i][j] = self.lista[num]
        return None

    def dibujarTablero(self, turno, puntos, actual, almacen):                                                                                               #Este método dibuja el teblero en pantalla
        abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R",
                      "S", "T", "U", "V", "W", "X", "Y", "Z"]
        print(end="   ")
        for i in range(self.col):
            print(i + 1, end="   ")
        print("")
        print(end=" ")
        for i in range(self.col):
            print("┌───", end="")
        print("┐")                                                                                                                                          #Imprime las líneas que le dan imagen a un tablero, en un principio, 6x6
        for i in range(self.fil):
            print(abecedario[i], end="")
            for j in range(self.col):
                print("│", self.matriz[i][j], end=" ")                                                                                                      #Introduce el elemento que tiene que ir dentro de la celda
            print("│", end="")
            print("")
            print(end=" ")
            for h in range(self.col):
                if i < self.fil - 1:
                    print("├───", end="")
            if i < self.fil - 1:
                print("┤")
        for k in range(self.col):
            print("└───", end="")
        print("┘")
        print(end=" ")
        print(f"Turno: {turno}", end=" ")                                                                                                                   #Imprime en pantalla los puntos,los turnos, el almacen y el elemento actual
        print(f"Puntos: {puntos}")
        print(f"Almacen: [{almacen}]", end=" ")
        print(f"Actual: [{actual}]")
        return None

    def ocupadaCord(self, coord, actual):                                                                                                                   #Este método comprueba que las coordenadas introducidas puedan ser ocupadas y, a su vez, que las coordenadas estén bien introducidas
        letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        posicion = 0
        if coord == '*':
            return False
        if coord=='':                                                                                                                                       #comprobamos que la cadena no esté vacía
            return True
        if coord[0] < 'A' or 'Z' < coord[0]:                                                                                                                #Comprueba que el primer elemento sea una letra mayúscula
            return True
        if len(coord) != 2:                                                                                                                                 #Comprueba que las coordenadas tengan longitud 2
            return True
        try:
            num = int(coord[1])
        except:
            return True
        for i in range(len(letras)):                                                                                                                        #Comprueba que las coordenadas introducidas estén disponibles
            if letras[i] == coord[0]:
                posicion = i
        if num > self.col or posicion + 1 > self.fil:
            return True
        else:
            if actual == 'W':                                                                                                                               #Comprueba que el Wick no se introduzca en una posicion vacia
                if self.matriz[posicion][num - 1] == '.':
                    return True
                else:
                    return False
            else:
                if self.matriz[posicion][num - 1] != '.':
                    return True
                else:
                    return False

    def colocarCord(self, coord,actual):                                                                                                                    # método que recibe las coordenadas y el elemento actual y lo coloca en la matriz
        letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"                                                                                                              # diccionario utilizado para operar con las coordenadas dadas
        posicion = 0                                                                                                                                        # inicializamos posición en 0
        num = int(coord[1])                                                                                                                                 # num es el segundo elemento de las coordenadas, es decir las Y de la matriz
        for i in range(len(letras)):                                                                                                                        # recorremos letras para que una vez que encuentre una letra que sea igual a la introducida en las coordenadas, nos devuelva su posición(las X de la matriz)
            if letras[i] == coord[0]:
                posicion = i
        if actual == 'W':                                                                                                                                   # si en actual tenemos un wick hay que operar de manera distinta
            if self.matriz[posicion][num - 1] == '1' or self.matriz[posicion][num - 1] == '2' or self.matriz[posicion][num - 1] == '3' or self.matriz[posicion][num - 1] == '4':  # si el elemento que vamos a quitar es parte de la cadena de los BF, eliminamos su edad del diccionario para evitar errores
                self.edadbigfoot.pop((posicion, num - 1), None)
            self.matriz[posicion][num - 1] = '.'                                                                                                            # introducimos el valor vacío en dicha posición que hemos eliminado

        else:
            self.matriz[posicion][num - 1] = actual                                                                                                         # sino es un wick, introducimos en la matriz el elemento actual
        return None

    def extraercoords(self,coord):                                                                                                                          # método usado para obtener las coordenadas del elemento introducido para operar en los siguientes métodod de colapso(se opera igual que en el método anterior)
        letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
        posicion = 0
        num = int(coord[1])
        for i in range(len(letras)):
            if letras[i] == coord[0]:
                posicion = i
        j = int(coord[1])
        return posicion, j - 1

    def confirmarcolapso(self, i, j, prox, i2, j2,visitados):                                                                                               # recibe las coordenadas del elemento introducido, las últimas coordenadas localizadas y la lista de visitados para evitar bucles infinitos
        if self.matriz[i][j] == 'a' or self.matriz[i][j] == 'b' or self.matriz[i][j] == 'c' or self.matriz[i][j] == 'd':                                    # si el elemento es a,b,c o d operamos
            visitados = list(visitados)                                                                                                                     # pasamos visitados  a lista para evitar errores
            visitados.append(f"{i}{j}")                                                                                                                     # introducimos las coordenadas actuales a dicha lista

            if i > 0 and (
            f"{i - 1}{j}") not in visitados:                                                                                                                # si puede haber un elemento arriba y además este no está en visitado, comprobamos
                if self.matriz[i][j] == self.matriz[i - 1][j] and i - 1 != i2:                                                                              # si el elemento de las coordenadas actuales es igual al de arriba y además ese no lo hemos visto anteriormente procedemos a continuar
                    prox = prox + 1                                                                                                                         # aumentamos el número de elementos próximos en 1
                    prox = self.confirmarcolapso(i - 1, j, prox, i, j,
                                                 visitados)                                                                                                 # aplicamos recursividad con las coordenadas del elemento de arriba
            if i < self.fil - 1 and (f"{i + 1}{j}") not in visitados:                                                                                       # en el resto de direcciones de opera igual
                if self.matriz[i][j] == self.matriz[i + 1][j] and i + 1 != i2:
                    prox = prox + 1
                    prox = self.confirmarcolapso(i + 1, j, prox, i, j, visitados)
            if j > 0 and (f"{i}{j - 1}") not in visitados:
                if self.matriz[i][j] == self.matriz[i][j - 1] and j - 1 != j2:
                    prox = prox + 1
                    prox = self.confirmarcolapso(i, j - 1, prox, i, j, visitados)
            if j < self.col - 1 and (f"{i}{j + 1}") not in visitados:
                if self.matriz[i][j] == self.matriz[i][j + 1] and j + 1 != j2:
                    prox = prox + 1
                    prox = self.confirmarcolapso(i, j + 1, prox, i, j, visitados)
        else:   
            prox = 0                                                                                                                                        # si los elementos son distintos de los que pueden colapsar devolvemos que prox es 0
        return prox

    def colapso1(self, i, j, prox, i2, j2,colapsados):                                                                                                      # método que va a añadir en una lista todos los elementos que pueden colapsar
        colapsados = list(colapsados)                                                                                                                       # opera igual que el método anterior, recogiendo los valores ya comprobados en la lista listocolap para evitar bucles infinitos y aplicando recursividad con las nuevas coordenadas
        colapsados.append(f"{i}{j}")
        listcolap = []
        if i > 0 and (f"{i - 1}{j}") not in colapsados:
            if self.matriz[i][j] == self.matriz[i - 1][j] and i - 1 != i2:
                listcolap.append(f"{i - 1}{j}")
                listcolap += self.colapso1(i - 1, j, prox, i, j, colapsados)
        if i < self.fil - 1 and (f"{i + 1}{j}") not in colapsados:
            if self.matriz[i][j] == self.matriz[i + 1][j] and i + 1 != i2:
                listcolap.append(f"{i + 1}{j}")
                listcolap += self.colapso1(i + 1, j, prox, i, j, colapsados)
        if j > 0 and (f"{i}{j - 1}") not in colapsados:
            if self.matriz[i][j] == self.matriz[i][j - 1] and j - 1 != j2:
                listcolap.append(f"{i}{j - 1}")
                listcolap += self.colapso1(i, j - 1, prox, i, j, colapsados)
        if j < self.col - 1 and (f"{i}{j + 1}") not in colapsados:
            if self.matriz[i][j] == self.matriz[i][j + 1] and j + 1 != j2:
                listcolap.append(f"{i}{j + 1}")
                listcolap += self.colapso1(i, j + 1, prox, i, j, colapsados)
        return listcolap

    def colapso2(self,listacoords, ):                                                                                                                       # recibe la lista de coordenadas calculada en el anterior apartado y opera en base a ella
        total = len(listacoords)                                                                                                                            # el número total de elementos juntos es igual a la longitud de dicha lista
        for i in range(total):                                                                                                                              # recorres la lista un número 'total' de veces
            coordenada = listacoords[i]                                                                                                                     # das a coordenada cada elemento de la lista que contendrá las coordenadas de los elementos a colapsar y les cambia el valor a un punto
            x = int(coordenada[0])
            y = int(coordenada[1])
            self.matriz[x][y] = "."
        return None

    def cambioelemento(self, i,j):                                                                                                                          # método que una vez los elementos que han colapsado de han transformado en un punto, cambia el elemento que hemos introducido a un elemento que lo colapse
        elemento = self.matriz[i][j]                                                                                                                        # obtiene el valor del elemento que hemos introducido en la posición dada
        if elemento == 'a':                                                                                                                                 # en base  a que elemento sea lo transforma en un valor que lo colapse
            self.matriz[i][j] = 'b'
        if elemento == 'b':
            self.matriz[i][j] = 'c'
        if elemento == 'c':
            self.matriz[i][j] = 'd'
        if elemento == 'd':
            self.matriz[i][j] = 'e'
        return None

    def puntosronda(self):                                                                                                                                  # calculamos los puntos por ronda recorriendo la matriz y sumando el valor exacto al total de puntos según con que valores se vaya encontrando(se actualiza cada ronda)
        puntos = 0
        for i in range(self.fil):
            for j in range(self.col):
                if self.matriz[i][j] == 'a':
                    puntos += 1
                if self.matriz[i][j] == 'b':
                    puntos += 5
                if self.matriz[i][j] == 'c':
                    puntos += 25
                if self.matriz[i][j] == 'd':
                    puntos += 125
                if self.matriz[i][j] == 'e':
                    puntos += 625
                if self.matriz[i][j] == '1':
                    puntos += -25
                if self.matriz[i][j] == '2':
                    puntos += -25
                if self.matriz[i][j] == '3':
                    puntos += 50
                if self.matriz[i][j] == '4':
                    puntos += 500
                if self.matriz[i][j] == 'X':
                    puntos += -50
                if self.matriz[i][j] == '.':
                    puntos += 0
        return puntos

    def colapsoBigFoot(self):                                                                                                                               # método para colapsar los BF
        for i in range(self.fil):                                                                                                                           # recorremos toda la matriz
            for j in range(self.col):
                encerrado = True                                                                                                                            # damos por supuesto que esta encerrado
                if self.matriz[i][j] == '1':                                                                                                                # si encontramos un BF comprobamos
                    if i > 0 and self.matriz[i - 1][
                        j] == '.':                                                                                                                          # si en cualquier direccion encontramos un '.' significa que no está encerrado
                        encerrado = False
                    elif j < self.col - 1 and self.matriz[i][j + 1] == '.':
                        encerrado = False
                    elif i < self.fil - 1 and self.matriz[i + 1][j] == '.':
                        encerrado = False
                    elif j > 0 and self.matriz[i][j - 1] == '.':
                        encerrado = False
                    if encerrado == True:                                                                                                                   # sino, lo colapsamos en un 2, y aumentamos por última vez su edad
                        self.matriz[i][j] = '2'
                        self.edadbigfoot[(i, j)] = self.edadbigfoot.get((i, j), 0) + 1
        return None

    def movimientoBigfoot(self):                                                                                                                            # método para realizar el movimiento de los BF
        unosmovidos = []                                                                                                                                    # guardamos los unos que hemos movido en esta lista para que un mismo uno no se mueva varias veces

        for i in range(self.fil):                                                                                                                           # recorremos la matriz hasta encontrarnos con un uno
            for j in range(self.col):
                if self.matriz[i][j] == '1':
                    if i > 0 and self.matriz[i - 1][j] == '.' and f"{i}{j}" not in unosmovidos:                                                             # si se puede mover hacia arriba, esa posición esta vacía y ademas ese uno todavía no se ha movido seguimos
                        unosmovidos.append(f"{i - 1}{j}")                                                                                                   # añadimos las coordenadas a donde se va a mover en la lista para que no se mueva mas de una vez
                        self.edadbigfoot[(i - 1, j)] = self.edadbigfoot.get((i, j),
                                                                            0) + 1                                                                          # incrementamos su edad, en caso de que aún no estuviera en el diccionario, lo añadimos con la edad 1
                        self.edadbigfoot.pop((i, j),None)                                                                                                   # eliminamos en caso de que ya estuviera en el diccionario, el elemento del diccionario que corresponde a su posición vieja
                        self.matriz[i - 1][j] = '1'
                        if self.edadbigfoot[(i - 1, j)] > 10:                                                                                               # si su edad es mayor o igual que 10, en su posición vieja dejamos un escombro
                            self.matriz[i][j] = 'X'
                        else:
                            self.matriz[i][j] = '.'                                                                                                         # sino, dejamos el espacio vacío('.')

                    elif j < self.col - 1 and self.matriz[i][j + 1] == '.' and f"{i}{j}" not in unosmovidos:                                                # realizamos el mismo método en todas las direcciones según el orden de prioridad(arriba,derecha,abajo,izquierda)
                        unosmovidos.append(f"{i}{j + 1}")
                        self.edadbigfoot[(i, j + 1)] = self.edadbigfoot.get((i, j), 0) + 1
                        self.edadbigfoot.pop((i, j), None)
                        self.matriz[i][j + 1] = '1'
                        if self.edadbigfoot[(i, j + 1)] > 10:
                            self.matriz[i][j] = 'X'
                        else:
                            self.matriz[i][j] = '.'
                    elif i < self.fil - 1 and self.matriz[i + 1][j] == '.' and f"{i}{j}" not in unosmovidos:
                        unosmovidos.append(f"{i + 1}{j}")
                        self.edadbigfoot[(i + 1, j)] = self.edadbigfoot.get((i, j), 0) + 1
                        self.edadbigfoot.pop((i, j), None)
                        self.matriz[i + 1][j] = '1'
                        if self.edadbigfoot[(i + 1, j)] > 10:
                            self.matriz[i][j] = 'X'
                        else:
                            self.matriz[i][j] = '.'

                    elif j > 0 and self.matriz[i][j - 1] == '.' and f"{i}{j}" not in unosmovidos:
                        unosmovidos.append(f"{i}{j - 1}")
                        self.edadbigfoot[(i, j - 1)] = self.edadbigfoot.get((i, j), 0) + 1
                        self.edadbigfoot.pop((i, j), None)
                        self.matriz[i][j - 1] = '1'
                        if self.edadbigfoot[(i, j - 1)] > 10:
                            self.matriz[i][j] = 'X'
                        else:
                            self.matriz[i][j] = '.'
        return None

    def colapsoBF1(self):                                                                                                                                   # método colapso de BF
        edadesordenadas = dict(self.edadbigfoot)                                                                                                            # para evitar errores transformamos nuevamente edadesordenadas en un diccionario

        for coordenadas, edades in edadesordenadas.items():                                                                                                 # pasamos cada una de las "claves" del diccionario al valor de coordenadas ya que estas claves son las coordenadas de los BF cuyo valor son las edades de dichos BF
            i, j = coordenadas                                                                                                                              # las coordenadas las pasamos a i,j para poder recorrer fácilmente la matriz
            edad = edades
            contador = 0                                                                                                                                    # contador de cuantos bebes hay juntos
            bbjunto = []                                                                                                                                    # variable creada para añadir los BF ya comprobados y evitar bucles infinitos
            if (self.matriz[i][j] == '2' and (f"{i}{j}") not in bbjunto):                                                                                   # si el BF de dicha coordenada ya es un bebe y aún no lo hemos comprobado seguimos
                bbjunto.append(f"{i}{j}")                                                                                                                   # lo añadimos a la lista para asegurarnos de no volver a él luego y entrar en un bucle infinito
                contador = contador + 1                                                                                                                     # aumentamos el contador de bebes juntos en 1

                def colapsoBF2(i,j):                                                                                                                        # entramos en un método anidado para comprobar los vecinos de los vecinos y así obtener todos y cada uno de los bebes que hay juntos
                    nonlocal bbjunto, contador                                                                                                              # nos aseguramos que bbjunto y contador no son variable locales de este método anidado
                    if (i > 0):                                                                                                                             # si i es mayor que 0, siginifica que puede haber un bebe en la posición de arriba
                        if (self.matriz[i - 1][j] == '2' and f"{i - 1}{j}" not in bbjunto):                                                                 # comprobamos que esto úñtimo sea cierto y en caso de ser cierto:
                            bbjunto.append(f"{i - 1}{j}")                                                                                                   # añadimos sus coordenadas a la lista, incrementamos el contador y aplicamos recursividad con dicho valor
                            contador = contador + 1
                            colapsoBF2(i - 1, j)
                    if (j < self.col - 1):                                                                                                                  # repetimos este mismo proceso para todas las direcciones posibles siguiendo el orden de prioridad(arriba,derecha,abajo,izquierda)
                        if (self.matriz[i][j + 1] == '2' and f"{i}{j + 1}" not in bbjunto):
                            bbjunto.append(f"{i}{j + 1}")
                            contador = contador + 1
                            colapsoBF2(i, j + 1)
                    if (i < self.fil - 1):
                        if (self.matriz[i + 1][j] == '2' and f"{i + 1}{j}" not in bbjunto):
                            bbjunto.append(f"{i + 1}{j}")
                            contador = contador + 1
                            colapsoBF2(i + 1, j)
                    if (j > 0):
                        if (self.matriz[i][j - 1] == '2' and f"{i}{j - 1}" not in bbjunto):
                            bbjunto.append(f"{i}{j - 1}")
                            contador = contador + 1
                            colapsoBF2(i, j - 1)
                    return bbjunto, contador                                                                                                                # devolvemos la lista con las coordenadas de los bebesjuntos y el número de bebes juntos que hay

                bbjunto, contador = colapsoBF2(i, j)                                                                                                        # llamamos a la función para obtener ambas variables
                if contador >= 3:                                                                                                                           # si hay mas de 3 bebes juntos procedemos a colapsar
                    edadmaxima = 0                                                                                                                          # variable que se actualizará para comprobar la edad máxima
                    for x, y in bbjunto:                                                                                                                    # extraemos las coordenadas de los bebes
                        edad = edadesordenadas[(int(x),int(y))]                                                                                             # obtenemos su edad a través del diccionario que la contiene y vamos actualizando la edad máxima en base a cual va siendo la mas alta
                        if edad > edadmaxima:
                            edadmaxima = edad
                    for x, y in bbjunto:                                                                                                                    # una vez se tiene la edad máxima recooremos otra vez todos los bebes, en caso de que la edad de dicho bebe sea la máxima lo sustituimos por un 3, y de no ser así desaparecen con un punto y se les elimina del diccionario de edades
                        if edadesordenadas[(int(x), int(y))] == edadmaxima:
                            self.matriz[int(x)][int(y)] = '3'
                        else:
                            self.matriz[int(x)][int(y)] = '.'
                            self.edadbigfoot.pop((int(x), int(y)), None)

        return None

    def colapsoBF4(self):                                                                                                                                   # este método funciona exactamente igual que el anterior pero cambiando que en lugar de actuar en los '2' para ccolapsar en '3', este colapsa los '3' en '4', pero siguiendo el mismo procedimiento
        edadesordenadas = dict(self.edadbigfoot)

        for coordenadas, edades in edadesordenadas.items():
            i, j = coordenadas
            edad = edades
            contador = 0
            bbjunto = []
            if (self.matriz[i][j] == '3' and (f"{i}{j}") not in bbjunto):
                bbjunto.append(f"{i}{j}")
                contador = contador + 1

                def colapsoBF3(i, j):
                    nonlocal bbjunto, contador
                    if (i > 0):
                        if (self.matriz[i - 1][j] == '3' and f"{i - 1}{j}" not in bbjunto):
                            bbjunto.append(f"{i - 1}{j}")
                            contador = contador + 1
                            colapsoBF3(i - 1, j)
                    if (j < self.col - 1):
                        if (self.matriz[i][j + 1] == '3' and f"{i}{j + 1}" not in bbjunto):
                            bbjunto.append(f"{i}{j + 1}")
                            contador = contador + 1
                            colapsoBF3(i, j + 1)
                    if (i < self.fil - 1):
                        if (self.matriz[i + 1][j] == '3' and f"{i + 1}{j}" not in bbjunto):
                            bbjunto.append(f"{i + 1}{j}")
                            contador = contador + 1
                            colapsoBF3(i + 1, j)
                    if (j > 0):
                        if (self.matriz[i][j - 1] == '3' and f"{i}{j - 1}" not in bbjunto):
                            bbjunto.append(f"{i}{j - 1}")
                            contador = contador + 1
                            colapsoBF3(i, j - 1)
                    return bbjunto, contador

                bbjunto, contador = colapsoBF3(i, j)
                if contador >= 3:
                    edadmaxima = 0
                    for x, y in bbjunto:
                        edad = edadesordenadas[(int(x), int(y))]
                        if edad > edadmaxima:
                            edadmaxima = edad
                    for x, y in bbjunto:
                        if edadesordenadas[(int(x), int(y))] == edadmaxima:
                            self.matriz[int(x)][int(y)] = '4'
                        else:
                            self.matriz[int(x)][int(y)] = '.'
                            self.edadbigfoot.pop((int(x), int(y)), None)
        return None

    def mapalleno(self):                                                                                                                                    # método comprueba si el mapa está lleno
        num = 0                                                                                                                                             # contador para comprobar
        for i in range(self.fil):                                                                                                                           # recorremos la matriz y en caso de encontrar un '.', el contador se incrementa
            for j in range(self.col):
                if self.matriz[i][j] == '.':
                    num = num + 1
        if num == 0:                                                                                                                                        # si el contador se ha incrementado, el tablero aún no está lleno, si no se ha incrementado si lo está
            return True
        else:
            return False


if __name__ == "__main__":                                                                                                                                  # comienza el programa con el main
    print("SUBURBIOUS!")
    prox = int(1)                                                                                                                                           # variable que usaremos para saber el número de vecinos
    tablero = Tablero()                                                                                                                                     # llamamos al objeto tablero
    tablero.crearTablero()                                                                                                                                  # creamos la matriz o "tablero"
    secuencia = Secuencia()                                                                                                                                 # llamamos al objeto que será la secuencia de datos que aparezcan
    tableroname = input(
        "Introduzca el nombre del tablero: ")                                                                                                               # pedimos al usuario que introduzca el nombre del fichero de tablero y de secuencia
    secname = input("Introduzca el nombre de fichero secuencia: ")
    try:                                                                                                                                                    # si el fichero del tablero existe lo abrimos e introducimos sus valores en la matriz previamente creada
        f = open(f"{tableroname}", "r")
        tablero.copiarTablero()
    except Exception:                                                                                                                                       # si no existe, llamamos al método llenartablero que nos creará un tablero aleatorio en base a las probabilidades que nos dieron en la hoja de la práctica
        tablero.llenarTablero()
    turno = 1                                                                                                                                               # inicializamos el turno en 1 y los puntos iniciales en 0
    puntos = tablero.puntosronda()                                                                                                                          # calculamos los puntos
    almacen = '.'                                                                                                                                           # el almacen al principio está vacío así que le damos el valor inicial de '.'
    temp = ''                                                                                                                                               # variable temporal que nos servirá para hacer el cambio del valor actual al almacen
    cambiar = False                                                                                                                                         # variable que usaremos para que cuando intercambiemos el almacen con el valor actual, los turnos no aumenten ni se muevan los BF
    edad = 0                                                                                                                                                # variable usada para la edad de los BF
    mapalleno = False                                                                                                                                       # variable usada para poder terminar la partida cuando todas las casillas estén llenas
    '''Aqui empieza turno'''
    while mapalleno == False:                                                                                                                               # mientras que haya casillas libres el juego sigue

        if (cambiar == False):                                                                                                                              # si no hemos cambiado los valores del almacén procedemos a comenzar el turno
            actual = secuencia.crearSecuencia(secname,turno)                                                                                                # llamamos al método crearSecuencia para que nos de el siguiente valor actual que podremos introducir en el tablero, en base al nombre del fichero de secuencia dado previamente
        cambiar = False                                                                                                                                     # en caso de que previamente hayamos intercambiado los valores de actual y almacen, volvemos a poner cambiar en falso
        tablero.dibujarTablero(turno, puntos, actual,almacen)                                                                                               # mostramos en pantalla el turno,los puntos,el valor actual,el almacen y el propio tablero con el método dibujar tablero
        coordenadas = input("Introduce las coordenadas: ")                                                                                                  # pedimos al usuario las siguientes coordenadas
        validacion = tablero.ocupadaCord(coordenadas,actual)                                                                                                # comprobamos que las coordenadas sean correctas y en caso de que no lo sean, las pedimos hasta que lo sean
        while validacion == True:
            coordenadas = input("ERROR Introduce las coordenadas: ")
            validacion = tablero.ocupadaCord(coordenadas, actual)
        if coordenadas == '*':                                                                                                                              # si el usuario teclea *, procedemos a intercambiar valores con el almacen
            if almacen == '.':                                                                                                                              # si el almacen está vacio, el valor actual se va al almacen y se genera un nuevo valor actual
                almacen = actual
                actual = secuencia.crearSecuencia(secname, turno)
            else:                                                                                                                                           # si el almacen está ocupado, intercambiamos su valor con actual, pasando por una variable intermedia para no perder datos
                cambiar = True
                temp = almacen
                almacen = actual
                actual = temp
        else:
            tablero.colocarCord(coordenadas,actual)                                                                                                         # si no hemos tecleado *, llamamos al método colocarCord e introducimos el valor de actual en el tablero
            resultad = tablero.extraercoords(coordenadas)                                                                                                   # y extraemos las coordenadas reales de dicho elemento que hemos introducido (A6-->05)
            for i in range(4):                                                                                                                              # realizamos el método de colapsar 4 veces ya que como máximo van a poder colapsar 4 veces(a-->b-->c--->d--->e)
                visitados = []                                                                                                                              # variable creada para almacenar las coordenadas ya comprobadas para evitar bucles infinitos en el siguiente método
                numerovecinos = tablero.confirmarcolapso(resultad[0], resultad[1], prox, resultad[0], resultad[1],visitados)                                # calculamos cuantos elementos próximos e iguales al valor introducido hay
                colapsados = []                                                                                                                             # tiene la misma función que visitados pero para el siguiente método
                if numerovecinos >= 3:                                                                                                                      # si hay 3 o más elementos iguales próximos procedemos a colapsar
                    listacoords = tablero.colapso1(resultad[0], resultad[1], prox, resultad[0], resultad[1],
                                                   colapsados)                                                                                              # método que en base a unas coordenadas, un número de elementos próximos y una lista, va recorriendo todos los elementos y sus vecinos y llenando una lista con sus coordenadas
                    tablero.colapso2(listacoords)                                                                                                           # en base a la anterior losta, transforma todos los valores de dichas coordenadas en '.' incluido el valor introducido por el usuario
                    tablero.cambioelemento(resultad[0], resultad[1])                                                                                        # transforma el valor introducido por el usuario en el elemento que lo colapsa(a-->b-->c-->d-->e)
            tablero.colapsoBigFoot()                                                                                                                        # comprobamos que no haya BF encerrados y de haberlos se transforman en 2 y el incremento de su edad y movimiento paran
            tablero.movimientoBigfoot()                                                                                                                     # si se pueden mover realizamos el movimiento además de que antes de dicho movimiento su edad se incrementa en 1 por cada turno
            tablero.colapsoBF1()                                                                                                                            # de haber 3 o más bebes de BF juntos estos se colapsan y se transforman en un 3 en la posición del bebe que tenga una mayor edad y el resto en un '.'
            tablero.colapsoBF4()                                                                                                                            # de haber 3 o más '3' juntos estos se colapsan y se transforman en un '4' en la posición del '3' que tenga una mayor edad y el resto en un '.'
            turno = turno + 1                                                                                                                               # se incrementa en uno el turno
        mapalleno = tablero.mapalleno()                                                                                                                     # se comprueba que el tablero esté lleno
        puntos = tablero.puntosronda()                                                                                                                      # se actualizan los puntos de dicha ronda
    print(f"Enhorabuena! Buena partida, tu puntuación es: {puntos}")                                                                                        # de haber terminado el juego, se notificia y se muestran los puntos totales al finalizar la partida
