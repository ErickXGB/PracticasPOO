# Compendio de Prácticas de Programación en Python
## Sistema Avanzado de Logística de Energía Solar Off-Grid y Monitoreo de Hardware

Este compendio reúne y reestructura una serie de ejercicios académicos bajo los principios de la **Programación Orientada a Objetos (POO)**, la modularización en paquetes y el tipado estático en Python. Todo el ecosistema está unificado bajo una temática técnica del mundo real: **Logística, Monitoreo y Auditoría de Estaciones de Energía Solar Fotovoltaica con Bancos de Baterías LiFePO4**.

El software cuenta con una interfaz de consola interactiva (CLI) blindada mediante secuencias de escape ANSI para renderizar marcos estáticos en color amarillo pastel, control posicional absoluto de caracteres mediante coordenadas y la limpieza del historial de *scrollback* de la terminal para emular el comportamiento de una aplicación nativa de escritorio.

Estudiante: Erick Xavier Gómez Burgos

---

## 1. Estructura Arquitectural del Proyecto

La topología del código sigue una estricta segmentación por responsabilidades (Núcleo de Interfaz vs Capas de Dominio Académico y Práctico):

```text
practica_experimental/
│
├── main.py                     # Punto de entrada y orquestador global del ciclo de vida del software.
│
├── core/                       # Núcleo del Sistema (Motor de Renderizado y UI)
│   ├── __init__.py
│   ├── console_ui.py           # Control posicional, limpieza de pantalla y búfer de scrollback.
│   └── menu_handler.py         # Control de marcos estáticos amarillo pastel y enrutamiento dinámico.
│
├── blocks/                     # Capa de Aplicación - Módulos por Bloques (0 al 17)
│   ├── block0/
│   │   ├── bloque0.py          # Menú y ejercicios de clase (Sistema de Biblioteca)
│   │   └── bloque0_practice.py # Práctica integradora: Abstracción Solar Base
│   ├── block1/
│   │   ├── bloque1.py          # Menú y ejercicios de clase (Constructores y Métodos)
│   │   └── bloque1_practice.py # Práctica integradora: Regulador de Carga Solar y Listas
│   ├── block2/
│   │   ├── bloque2.py          # Menú y ejercicios de clase (Tipos de datos y Slicing)
│   │   └── bloque2_practice.py # Práctica integradora: Telemetría Estructural Solar
│   ├── block3/
│   │   ├── bloque3.py          # Menú y ejercicios de clase (Precedencia de Operadores)
│   │   └── bloque3_practice.py # Práctica integradora: Balance de Carga LiFePO4 e Identidad
│   ├── block4/
│   │   ├── bloque4.py          # Menú y ejercicios de clase (Manejo de Entrada/Salida)
│   │   └── bloque4_practice.py # Práctica integradora: Registro de Telemetría con Blindaje Input
│   ├── block5/
│   │   ├── bloque5.py          # Menú y ejercicios de clase (Estructuras de Control)
│   │   └── bloque5_practice.py # Práctica integradora: Lógica BMS y Desconexión Booleana
│   ├── block6/
│   │   ├── bloque6.py          # Menú y ejercicios de clase (Estructuras de Bucles)
│   │   └── block6_practice.py # Práctica integradora: Ciclo Solar Diario y List Comprehension
│   ├── block7/
│   │   ├── bloque7.py          # Menú y ejercicios de clase (Declaración de Funciones)
│   │   └── bloque7_practice.py # Práctica integradora: Pérdidas por Cableado y Retorno Modular
│   ├── block8/
│   │   ├── bloque8.py          # Menú y ejercicios de clase (Métodos de Listas Mutables)
│   │   └── bloque8_practice.py # Práctica integradora: Analizador de Picos y Métodos Estadísticos
│   ├── block9/
│   │   ├── bloque9.py          # Menú y ejercicios de clase (Uso de Tuplas de Solo Lectura)
│   │   └── bloque9_practice.py # Práctica integradora: Geolocalización Fija y Auditoría de Logs
│   ├── block10/
│   │   ├── bloque10.py         # Menú y ejercicios de clase (Estructuras Llave-Valor)
│   │   └── bloque10_practice.py# Práctica integradora: Registro de Inversor e Iteradores Nativos
│   ├── block11/
│   │   ├── bloque11.py         # Menú y ejercicios de clase (Fundamentos de Conjuntos)
│   │   └── bloque11_practice.py# Práctica integradora: Álgebra de Sets y Unicidad de Hardware
│   ├── block12/
│   │   ├── bloque12.py         # Menú y ejercicios de clase (Manejo de Excepciones)
│   │   └── bloque12_practice.py# Práctica integradora: Trampa de Errores Específicos y Finally
│   ├── block13/
│   │   ├── bloque13.py         # Menú y ejercicios de clase (Fundamentos de Decoradores)
│   │   └── bloque13_practice.py# Práctica integradora: Decoradores de Telemetría y Wrapper Comodín
│   ├── block14/
│   │   ├── bloque14.py         # Menú y ejercicios de clase (Mecánicas de Unpacking)
│   │   └── bloque14_practice.py# Práctica integradora: Desempaquetado Estructural y Operador Asterisco
│   ├── block15/
│   │   ├── bloque15.py         # Menú y ejercicios de clase (Funciones de Orden Superior)
│   │   └── bloque15_practice.py# Práctica integradora: Filtrado y Mapeo Funcional con Lambda
│   ├── block16/
│   │   ├── bloque16.py         # Menú y ejercicios de clase (Efecto de Persistencia)
│   │   └── bloque16_practice.py# Práctica integradora: Serialización y Lectura de Archivos JSON
│   └── block17/
│       ├── bloque17.py         # Menú y ejercicios de clase (Fundamentos de Mixins)
│       └── bloque17_practice.py# Práctica integradora final: Composición con Mixins Avanzados
│
└── files/                      # Almacenamiento persistente local (Generado dinámicamente)
    └── data.json               # Manejo básico con JSON
    └── helloworld.txt          # Manejo básico de archivos
    └── telemetria.json         # Logs estructurados en disco duro
    └── users.json              # Manejo básico con JSON


## 2. Documentación detallada

### BLOQUE 0: INTRODUCCIÓN A LA POO

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo estructurar un archivo controlador en Python que almacene múltiples funciones de prueba independientes, contenga clases base como Person y asocie todo a un diccionario de opciones para un menú interactivo."
* **Prompt para un proceso similar:**
  > "Cómo modelar una clase en Python bajo POO que represente una entidad física del mundo real, aplicando abstracción para define sus propiedades técnicas iniciales con tipado estático."
* **Resolución Propia:** Contiene los ejercicios de clase (`bloque0.py`) que implementan el diseño de una biblioteca virtual, la instanciación de objetos de la clase `Person` (`run_exercise_2`) y la teoría base de la POO. Asimismo, integra el archivo de práctica (`bloque0_practice.py`) el cual modela la clase `SolarArrayPractice` como plano abstracto y utiliza `SolarStationMonitor` para inicializar y desplegar la configuración estructural de un arreglo fotovoltaico de 800W.

### BLOQUE 1: CONSTRUCTOR \_\_init\_\_

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo implementar métodos alternativos de construcción en una clase de Python utilizando el decorador classmethod para instanciar objetos a partir de estructuras de datos como diccionarios."
* **Prompt para un proceso similar:**
  > "Diseña una clase en Python que reciba parámetros en su constructor dunder init, maneje colecciones internas y proporcione un constructor alternativo usando @classmethod para cargar datos, aplicando estos conceptos al almacenamiento de un historial dinámico mediante append."
* **Resolución Propia:** Organiza los ejercicios base de clase (`bloque1.py`) encargados de instanciar objetos de la clase `Student` con paso de notas y ejecutar constructores alternativos mediante `@classmethod`. Además, incorpora el archivo de práctica (`bloque1_practice.py`) el cual implementa la clase `ChargeControllerPractice` para inicializar parámetros de un regulador MPPT de 30A, utilizando un método de clase para configurar bancos LiFePO4 de 12V y guardando lecturas dinámicas de potencia con `.append()`.

### BLOQUE 2: VARIABLES Y TIPOS DE DATOS

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo inspeccionar los tipos de variables nativas simples y complejas en Python usando la función type() y aplicar operaciones de segmentación o slicing sobre índices de colecciones."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio en Python que declare variables de tipos simples y complejos, demuestre el uso de slicing en una lista de 5 elementos para extraer extremos e intervalos, e incluya la declaración de estructuras locales como diccionarios dentro de un método aislado."
* **Resolución Propia:** Consolida las rutinas de clase (`bloque2.py`) orientadas a la inspección de tipos mediante `type()` y segmentación básica de arreglos. A su vez, integra el archivo de práctica (`bloque2_practice.py`) el cual instancia la clase `SolarDataManager`, aplicando técnicas de *slicing* sobre muestras de voltaje de baterías extraídas de una lista e inicializando diccionarios locales de diagnóstico térmico dentro de un método de control.

### BLOQUE 3: OPERADORES

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo evaluar la precedencia de operadores aritméticos en Python y contrastar el comportamiento del operador de igualdad estructural frente al operador de identidad de objetos en memoria RAM."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python que demuestre operadores aritméticos (incluyendo división entera, módulo y potencia), operadores de comparación e identidad (== vs is), y resuelva una ecuación respetando la jerarquía de operadores."
* **Resolución Propia:** Resuelve las operaciones matemáticas del compendio. Conecta los scripts base y el archivo de práctica (`bloque3_practice.py`) para diseñar la clase `BatteryBalanceManager`, encargada de ejecutar operaciones aritméticas complejas sobre un banco de energía y auditar celdas de litio independientes para comprobar la separación de punteros en la memoria RAM mediante el uso de `is`.

### BLOQUE 4: ENTRADA Y SALIDA DE DATOS

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo estructurar un bucle de captura interactiva que use tipado dinámico y casting seguro para interceptar ValueErrors causados por entradas del usuario alfanuméricas inválidas."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase que capture mediante input parámetros de texto y numéricos (float e int) aplicando validación estricta con loops while True y bloques try/except para evitar datos corruptos o negativos."
* **Resolución Propia:** Enlaza las funciones de entrada estándar junto con el archivo de práctica (`bloque4_practice.py`), el cual construye la clase `SolarTelemetryInput`. Esta unidad retiene el flujo en bucles de validación persistente ante fallas de casteo (`ValueError`) hasta recibir datos numéricos óptimos, imprimiendo reportes tabulados con máscaras de formato fijo en f-strings.

### BLOQUE 5: CONDICIONALES

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo encadenar condiciones múltiples condicionales lógicas en Python asociando operadores relacionales con operadores lógicos booleanos and, or y not."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase que valide un parámetro flotante y clasifique su estado en múltiples rangos mediante if/elif/else, y evalúe una desconexión de seguridad usando operadores lógicos and/or/not basados en múltiples sensores simultáneos."
* **Resolución Propia:** Acopla los condicionales académicos del módulo con el archivo de práctica (`bloque5_practice.py`). Este último codifica la clase `BatteryGuardBMS`, la cual actúa como un cerebro de protección industrial que analiza el estado de las celdas y dispara interruptores lógicos de corte de energía ante anomalías concurrentes en el hardware.

### BLOQUE 6: BUCLES

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo explotar el rendimiento de las comprensiones de listas en Python para filtrar secuencias numéricas y contrastar su sintaxis frente a bucles iterativos tradicionales."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase que use un bucle while para simular el paso del tiempo, un bucle for con enumerate() para auditar elementos indexados, y una List Comprehension para generar los cuadrados de una lista bajo una condición matemática."
* **Resolución Propia:** Agrupa las iteraciones base del bloque con el archivo de práctica (`bloque6_practice.py`). El módulo desarrolla la clase `SolarCycleSimulator`, encargada de mapeo de canales de consumo indexados mediante `enumerate()` y de calcular armónicos eficientes de potencia filtrados mediante expresiones veloces de *List Comprehension*.

### BLOQUE 7: FUNCIONES

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómoiseñar subprogramas modulares encapsulados en métodos de instancia que manipulen argumentos posicionales y devuelvan resultados procesados mediante la instrucción return."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase que demuestre el uso de métodos sin parámetros, métodos con parámetros posicionales y el uso estricto de la sentencia return para devolver valores calculados hacia el flujo principal."
* **Resolución Propia:** Conecta la modularización del bloque con el archivo de práctica (`bloque7_practice.py`). Implementa la clase `SolarFunctionManager`, la cual aísla las funciones procedimentales de interfaz del núcleo matemático encargado de procesar y retornar las pérdidas eléctricas por cableado mediante la sentencia `return`.

### BLOQUE 8: LISTAS

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo manipular una colección ordenada mutable en Python aplicando métodos de ordenamiento de orden interno y funciones integradas de agregación estadística."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase que inicialice una lista vacía en su constructor, añada elementos con append(), organice los datos con sort() y extraiga la suma total, el máximo y el mínimo usando funciones nativas."
* **Resolución Propia:** Consolida el manejo de arreglos mutables con el archivo de práctica (`bloque8_practice.py`). Estructura la clase `SolarLoadAnalyzer` alimentando un almacén de consumo eléctrico dinámico con `.append()`, ordenándolo de menor a mayor con `.sort()` y extrayendo analíticas de picos energéticos con `sum()`, `max()` y `min()`.

### BLOQUE 9: TUPLAS

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo explotar los métodos de las tuplas inmutables en Python para examinar frecuencias y posiciones de elementos constantes dentro de secuencias protegidas."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase que almacene constantes fijas en una tupla, y demuestre el uso de los métodos nativos .count() para auditar elementos repetidos y .index() para hallar la posición exacta de un registro."
* **Resolución Propia:** Mapea las secuencias de solo lectura del bloque junto al archivo de práctica (`bloque9_practice.py`). Implementa `SolarTupleManager`, clase encargada de fijar coordenadas geo-satitales inmutables de la planta e inspeccionar el historial de fallas del sistema mediante llamadas síncronas a `.count()` y `.index()`.

### BLOQUE 10: DICCIONARIOS

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo iterar sobre mapas estructurados llave-valor en Python diseccionando de forma independiente sus componentes estructurales mediante métodos iteradores asociativos."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase que inicialice un diccionario con parámetros mixtos, permita actualizar e inyectar llaves dinámicamente y use de forma exhaustiva los métodos .keys(), .values() y .items() para imprimir reportes."
* **Resolución Propia:** Liga las colecciones asociativas del bloque con el archivo de práctica (`bloque10_practice.py`). Codifica `SolarInverterRegistry` administrando los parámetros dinámicos de un inversor híbrido y desglosando la información a través de recorridos sobre `.keys()`, `.values()` e `.items()`.

### BLOQUE 11: CONJUNTOS

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo aplicar operaciones algebraicas de teoría de conjuntos sobre colecciones hash de elementos únicos utilizando operadores bitwise en Python."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase que inicialice dos conjuntos (sets) con elementos duplicados para demostrar la unicidad automática, y aplique las operaciones de Unión (|), Intersección (&) y Diferencia (-) para generar listados."
* **Resolución Propia:** Integra los ejercicios académicos con el archivo de práctica (`bloque11_practice.py`). Desarrolla `SolarSetManager` purgando marcas de hardware redundantes gracias a la naturaleza del `set` y calculando compatibilidades de catálogos mediante álgebra de conjuntos con `|`, `&` y `-`.

### BLOQUE 12: MANEJO DE EXCEPCIONES (TRY / EXCEPT)

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo estructurar una pirámide de captura defensiva de excepciones en Python aislando errores matemáticos de errores de casteo y asegurando la ejecución de directivas de cierre."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase que implemente un bloque try/except estructurado para deparar y atrapar específicamente ZeroDivisionError y ValueError, incluyendo además la cláusula finally para asegurar la ejecución de un protocolo."
* **Resolución Propia:** Une la gestión de estabilidad del bloque con el archivo de práctica (`bloque12_practice.py`). Implementa `SolarExceptionAnalyzer` aislando desviaciones por cortocircuito infinito (`ZeroDivisionError`) y entradas alfanuméricas corruptas (`ValueError`), obligando al cierre seguro de compuertas eléctricas en el bloque `finally`.

### BLOQUE 13: DECORADORES

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómoiseñar funciones de orden superior en Python que actúen como envolturas de interceptación para inyectar comportamientos antes y después de la ejecución de métodos de instancia."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una función decoradora fuera de la clase llamada log_inverter_action que intercepte un método, imprima registros de inicio, ejecute la función original y cierre el ciclo, aplicándolo con la sintaxis @."
* **Resolución Propia:** Acopla las funciones avanzadas del módulo con el archivo de práctica (`bloque13_practice.py`). Diseña el decorador `log_inverter_action` usando parámetros comodín para envolver rutinas críticas de hardware en la clase `SolarOperationManager`, abstrayendo la lógica de logs de forma transparente.


### BLOQUE 14: DESEMPAQUETADO (UNPACKING)

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo realizar asignaciones múltiples masivas en Python segmentando colecciones iterables mediante destructuración posicional fija y el uso extendido del operador asterisco."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase llamada SolarUnpackingManager que almacene una lista de lecturas y demuestre el desempaquetado tradicional de elementos fijos, así como el desempaquetado avanzado usando el operador asterisco (*rest)."
* **Resolución Propia:** Conecta la asignación múltiple del bloque con el archivo de práctica (`bloque14_practice.py`). Desarrolla `SolarUnpackingManager` extrayendo parámetros de sensores mediante desempaquetado síncrono e hilando lecturas intermedias de amperaje mediante agrupamiento dinámico con el operador asterisco.

### BLOQUE 15: FUNCIONES DE ORDEN SUPERIOR

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo encadenar transformaciones de datos en colecciones de Python utilizando funciones integradas del paradigma funcional en combinación con predicados de funciones anónimas."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase llamada SolarFunctionalProcessor que administre una lista de potencias, e implemente de forma estricta la función filter() con una expresión lambda para extraer lecturas bajas, y la función map() con otra lambda para transformar unidades."
* **Resolución Propia:** Vincula las herramientas funcionales con el archivo de práctica (`bloque15_practice.py`). Codifica `SolarFunctionalProcessor` procesando matrices numéricas mediante programación funcional limpia: filtra anomalías con `filter()` y escala potencias métricas a Kilovatios con `map()` usando expresiones `lambda`.

### BLOQUE 16: ARCHIVOS Y JSON

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "Cómo serializar y deserializar diccionarios de memoria RAM hacia formatos físicos de texto almacenados en directorios del sistema operativo gestionando streams de datos seguros."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea una clase llamada SolarJsonManager que verifique si existe una carpeta usando os.path, guarde un diccionario usando json.dump(), e emplemente un método para leer ese mismo archivo con json.load()."
* **Resolución Propia:** Conecta los sistemas de persistencia con el archivo de práctica (`bloque16_practice.py`). Implementa `SolarJsonManager` controlando la persistencia de datos en la planta solar. Escribe configuraciones en formato plano tabulado con `json.dump()` y las recupera reconstruyendo el mapeo con `json.load()`.

### BLOQUE 17: MIXINS

* **IA Utilizada:** Gemini
* **Prompt utilizado para entender y resolver el ejercicio:**
  > "La manera correcta de estructurar clases utilitarias Mixin sin estados ni métodos constructores init para inyectar capacidades genéricas a clases de negocio mediante herencia múltiple."
* **Prompt para un proceso similar:**
  > "Ayúdame a diseñar un ejercicio práctico utilizando POO en Python. Crea dos clases Mixin sin constructores: JSONExportMixin (que use vars() para serializar atributos a JSON string) y SafetyAuditMixin (que evalúe rangos de seguridad), implementando una clase de negocio que herede de ambos."
* **Resolución Propia:** Corona el compendio integrando las clases de herencia del módulo con el archivo de práctica (`bloque17_practice.py`). Desarrolla la clase de negocio `AdvancedSolarArray` asimilando el comportamiento utilitario inyectado por herencia múltiple desde `JSONExportMixin` (extrayendo diccionarios de instancia mediante `vars(self)`) y `SafetyAuditMixin` para auditorías perimetrales eléctricas.

## 3. Mapa de Navegación entre Menús

[ MENÚ GENERAL - PRÁCTICA EXPERIMENTAL ] (Limpia pantalla y borra scrollback)
   │
   ├── [0] Bloque 0: Introducción a POO ──> [ Submenú Bloque 0 ] ──> Retorno con Enter
   ├── [1] Bloque 1: Constructor __init__ ──> [ Submenú Bloque 1 ] ──> Retorno con Enter
   ├── [2] Bloque 2: Variables y tipos de datos ──> [ Submenú Bloque 2 ] ──> Retorno con Enter
   ├── ...
   ├── [16] Bloque 16: Archivos y JSON ──> [ Submenú Bloque 16 ] ──> Retorno con Enter
   ├── [17] Bloque 17: Mixins ──> [ Submenú Bloque 17 ] ──> Retorno con Enter
   │
   └── [x] Salir (Cierra la aplicación de consola)


   