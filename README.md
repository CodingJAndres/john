# Menú de Comandos de John the Ripper

Este script en Python proporciona un menú interactivo para ejecutar varios comandos de [John the Ripper](https://www.openwall.com/john/), una popular herramienta de crackeo de contraseñas. El menú permite al usuario seleccionar diferentes opciones para ejecutar John the Ripper con varios parámetros.

## Requisitos

- Python 3.x
- John the Ripper (debe estar instalado en tu sistema y disponible en la línea de comandos)

## Instalación

1. **Clona o descarga el repositorio:**

    ```bash
    git clone https://github.com/CodingJAndres/john.git
    ```

2. **Navega al directorio del proyecto:**

    ```bash
    cd john
    ```

3. **Asegúrate de que John the Ripper esté instalado en tu sistema. Puedes descargarlo e instalarlo desde [aquí](https://www.openwall.com/john/).**

## Uso

1. **Ejecuta el script:**

    ```bash
    python john_the_ripper.py
    ```

2. **Selecciona una opción del menú:**

    - **1. Ejecutar John con lista de palabras:** Ejecuta John the Ripper utilizando un archivo de lista de palabras para la recuperación de contraseñas.
    - **2. Ejecutar John con ataque incremental:** Ejecuta John the Ripper utilizando un ataque incremental, que prueba todas las combinaciones posibles de caracteres.
    - **3. Ejecutar John con reglas:** Ejecuta John the Ripper aplicando reglas adicionales sobre una lista de palabras.
    - **4. Mostrar resultados de John:** Muestra los resultados de un ataque previamente ejecutado.
    - **5. Mostrar configuración actual de John:** Muestra la configuración actual de John the Ripper.
    - **6. Ejecutar John con un ataque específico:** Permite seleccionar el tipo de ataque (brute, mask o dictionary) y proporciona los parámetros necesarios.
    - **7. Salir:** Sale del menú y cierra el programa.

## Descripción de Opciones

- **Ejecutar John con lista de palabras:** Solicita el archivo de hash y el archivo de lista de palabras para realizar un ataque basado en diccionario.
- **Ejecutar John con ataque incremental:** Realiza un ataque incremental, que prueba todas las combinaciones posibles de caracteres.
- **Ejecutar John con reglas:** Aplica reglas adicionales a un archivo de lista de palabras para mejorar los intentos de crackeo.
- **Mostrar resultados de John:** Muestra los resultados del crackeo para un archivo de hash especificado.
- **Mostrar configuración actual de John:** Muestra la configuración de John the Ripper en tu sistema.
- **Ejecutar John con un ataque específico:** Permite elegir entre un ataque de fuerza bruta (`brute`), máscara (`mask`), o diccionario (`dictionary`) y ejecuta John the Ripper con los parámetros seleccionados.

## Manejo de Errores

- **KeyboardInterrupt:** El script maneja la interrupción del teclado (Ctrl+C) para cerrar el programa de manera segura.
- **FileNotFoundError:** Muestra un mensaje si un archivo no se encuentra en la ruta especificada.
- **Excepciones Generales:** Captura y muestra cualquier otro error que pueda ocurrir durante la ejecución del script.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---

¡Utiliza este script para administrar y ejecutar John the Ripper de manera más eficiente!
