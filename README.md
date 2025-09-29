# 🎮 SUBURBIOUS

**SUBURBIOUS** es un juego desarrollado en **Python** como práctica de primer curso de Ingeniería Informática.  
Se inspira en mecánicas de juegos tipo *Candy Crush*, pero incorpora elementos propios como evolución de caracteres y gestión de enemigos (Bigfoots).  

---

## 🕹️ Mecánicas principales
- El tablero es de **6x6** con caracteres que evolucionan:  
  `a → b → c → d → e`  
  Cuando se juntan 3 o más caracteres iguales, colapsan y se transforman en el de nivel superior.  

- **Bigfoots y evolución:**  
  - **1 → Bigfoot libre**  
    - Se mueve en 4 direcciones posibles siguiendo este orden de prioridad: **arriba → derecha → abajo → izquierda**.  
    - Envejece +1 cada turno.  
    - Al llegar a **edad 10** se convierte en un **escombro (X)** que bloquea permanentemente la celda.  
  - **2 → Bigfoot encerrado**  
    - Aparece cuando un `1` queda rodeado en todas direcciones.  
    - Deja de envejecer y ya no puede moverse.  
    - **3 o más "2" juntos colapsan en un `3` (casa).**  
  - **3 → Casa**  
    - Representa un conjunto de Bigfoots encerrados.  
    - **3 o más "3" juntos colapsan en un `4` (hotel).**  
  - **4 → Hotel**  
  - **X → Escombro**  
    - Celda bloqueada que no se puede eliminar.  

- El objetivo del juego es **aguantar el mayor número de turnos y alcanzar la máxima puntuación posible**.  

---

## 📂 Configuración inicial
Al iniciar el juego se puede elegir:  
- **Un fichero de tablero inicial**: define el estado inicial del tablero.  
- **Un fichero de secuencia**: define el orden en el que aparecerán los elementos a colocar.  

👉 Si no se introducen o son inválidos, el tablero y la secuencia se generarán de forma **aleatoria**.  

---

## 📦 Almacén
El jugador dispone de un **almacén** para guardar temporalmente una ficha:  
- Pulsando `*` en lugar de colocar la ficha actual, esta se guarda en el almacén.  
- Solo puede haber **una ficha almacenada a la vez**.  
- Para intercambiar la ficha actual con la del almacén se vuelve a usar `*`.  
- Si el almacén está vacío, la ficha actual se guarda y se genera una nueva.  

---

## ⏳ Flujo de un turno
Si no se utiliza el almacén, cada turno sigue este orden:  
1. El jugador coloca la ficha actual en el tablero.  
2. Se comprueban las **fusiones de casillas** (ej: `a+a+a → b`).  
3. Si algún **Bigfoot libre (1)** ha quedado encerrado, se transforma en **2**.  
4. Los **Bigfoots libres (1)** que no estén encerrados se mueven en orden de prioridad: arriba → derecha → abajo → izquierda.  
5. Se procesan los **colapsos de Bigfoots, casas y hoteles**:  
   - `2+2+2 → 3 (casa)`  
   - `3+3+3 → 4 (hotel)`  
6. Se recalculan los **puntos de la ronda**.  

---

## 🏆 Sistema de puntuación
- `a = +1`  
- `b = +5`  
- `c = +25`  
- `d = +125`  
- `e = +625`  
- `1 (Bigfoot libre) = -25`  
- `2 (Bigfoot encerrado) = -25`  
- `3 (Casa) = +50`  
- `4 (Hotel) = +500`  
- `X (Escombro) = -50`  

---

## ⚙️ Tecnologías
- Lenguaje: **Python 3**  
- Librerías: `random` (para generación aleatoria)  

---

## 🚀 Ejecución
1. Clonar el repositorio
2. Ejecutar el juego: python suburbious.py

---

## 📖 Controles
- Introducir coordenadas (ej: A3) para colocar el carácter actual en esa celda.
- Pulsar * para usar el almacén (guardar o intercambiar fichas).

---

## ✨ Aprendizaje

Este proyecto me permitió:

1. Practicar programación orientada a objetos en Python.
2. Desarrollar la lógica de un juego de tablero con mecánicas emergentes.
3. Implementar un sistema de evolución y colapso de elementos.
4. Diseñar una "IA" simple de enemigos con movimiento en 4 direcciones y envejecimiento progresivo.
5. Integrar la gestión de archivos de configuración externos (tablero y secuencia).

---

## 👥 Autores

- Proyecto desarrollado en colaboración por:

  - Marcos Alonso Ulloa

  - Marcau Cámara Vicente
