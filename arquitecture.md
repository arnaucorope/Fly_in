PARSER:
    - Leer el archivo del mapa.
    - Interpretar y validar cada línea según las reglas del subject.
    - Gestionar los errores indicando la línea y la causa.
    - Dejar los datos preparados para construir el grafo:
        - Número de drones.
        - Nodos con sus coordenadas y metadatos.
        - Conexiones con sus metadatos.
    - No se encargará de mover drones ni de ejecutar la simulación.

NODE:
    - Representar un nodo individual del grafo.
    - Guardar sus atributos:
        - Nombre.
        - Coordenadas X e Y.
        - Tipo de zona.
        - Color.
        - Capacidad máxima de drones.
        - Conexiones con otros nodos.
    - Permitir consultar la información del nodo.
    - PENDIENTE: decidir si el nodo guardará los drones que
      lo ocupan o si esa información estará en Simulation.

CONNECTION:
    - Representar una conexión bidireccional entre dos nodos.
    - Guardar:
        - Referencias a los dos nodos que conecta.
        - Capacidad máxima de la conexión.
    - Permitir consultar qué nodos conecta.
    - No decidirá qué drones pueden moverse ni cuándo.

DRONE:
    - Representar un dron individual.
    - Crear tantos objetos Drone como indique el archivo.
    - Guardar:
        - Identificador del dron.
        - Estado actual: en un nodo, atravesando una conexión
          o llegado a END.
    - PENDIENTE: decidir dónde se almacenará la ruta asignada
      a cada dron.

GRAPH:
    - Representar el mapa completo.
    - Guardar los nodos en un diccionario:
        - Clave: nombre del nodo.
        - Valor: objeto Node correspondiente.
    - Guardar y organizar las conexiones del mapa.
    - Permitir:
        - Añadir nodos.
        - Registrar conexiones entre nodos existentes.
        - Buscar un nodo por su nombre.
        - Consultar los vecinos de un nodo.
    - Facilitar que otras clases accedan al mapa completo
      mediante un único objeto Graph.

SIMULATION:
    - Recibir el objeto Graph y los drones ya construidos.
    - Gestionar el estado de la simulación.
    - Ejecutar los turnos hasta que todos los drones lleguen a END.
    - En cada turno:
        - Consultar los movimientos posibles.
        - Comprobar las capacidades de nodos y conexiones.
        - Gestionar los desplazamientos hacia zonas restricted.
        - Actualizar el estado de los drones.
    - Detectar cuándo ha terminado la simulación.
    - Proporcionar la información necesaria para representar
      cada turno en el Renderer.
    - No se encargará de leer el archivo ni de dibujar el mapa.
    - PENDIENTE: decidir cómo se integrará el algoritmo
      encargado de calcular y asignar rutas.

RENDER:
    - Recibir la información del grafo y de la simulación.
    - Dibujar los nodos y las conexiones utilizando sus coordenadas.
    - Representar visualmente los drones.
    - Animar los movimientos entre los estados de cada turno.
    - Los drones se representarán como naves de Rick y Morty.
    - Los nodos se representarán como portales verdes característicos.
    - No decidirá las rutas ni modificará el estado de la simulación.

MAIN:
    - Coordinar la preparación y ejecución del programa.
    - Utilizar Parser para leer y validar el archivo.
    - Construir el objeto Graph a partir de los datos validados.
    - Crear los objetos Drone.
    - Crear e iniciar Simulation con el grafo y los drones.
    - Iniciar y coordinar la visualización mediante Render.

STRUCTURE:
    fly_in/
├── main.py
├── parser/
│   ├── grammar.lark
│   ├── parser.py
│   └── models.py
├── graph/
│   ├── graph.py
│   ├── node.py
│   └── connection.py
├── simulation/
│   ├── drone.py
│   └── simulation.py
├── render/
│   └── renderer.py
├── assets/
└── tests/
