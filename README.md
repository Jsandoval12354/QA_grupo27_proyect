
# Pruebas de la API de Urban Grocers - Gestión de Kits

Este proyecto se enfoca en la automatización de pruebas para la funcionalidad de gestión de "kits" dentro de la API de la aplicación Urban Grocers, cubriendo las operaciones de creación, lectura (obtener todos), actualización y eliminación (CRUD). El objetivo principal es verificar que la API responda correctamente a diferentes tipos de solicitudes para estas operaciones, especialmente en lo referente al campo "name".

## Documentación de la API Utilizada

La documentación de la API utilizada para entender el funcionamiento de los endpoints de gestión de kits (`/api/v1/kits` para GET y POST, `/api/v1/kits/:id` para PUT y `/api/v1/kits/7` para DELETE) fue la interfaz Swagger que se encuentra disponible al acceder a la URL del servidor proporcionada por TripleTen y añadir `/docs/`. Aunque la lista de comprobación recomienda `apiDoc`, la documentación proporcionada era en formato Swagger.

## Tecnologías Utilizadas

* **Python:** El lenguaje de programación principal para escribir las pruebas.
* **requests:** Una biblioteca de Python utilizada para realizar las solicitudes HTTP a la API de Urban Grocers.
* **pytest:** Un framework de Python que facilita la escritura y ejecución de pruebas de manera organizada.

## Ejecución de las Pruebas

Para ejecutar las pruebas en tu entorno local, sigue estos sencillos pasos:

1.  Asegúrate de tener Python instalado en tu sistema.
2.  Instala las dependencias necesarias ejecutando el siguiente comando en tu terminal:
    ```bash
    pip install requests pytest
    ```
3.  Navega hasta la raíz del proyecto en tu terminal (la carpeta `qa-project-Urban-Grocers-app-es`).
4.  Ejecuta las pruebas con el siguiente comando:
    ```bash
    pytest
    ```

    Pytest buscará y ejecutará automáticamente todos los archivos y funciones de prueba dentro del proyecto, mostrando los resultados en la terminal.

Este conjunto de pruebas valida el comportamiento de los endpoints de gestión de kits, asegurando que las respuestas de la API sean las esperadas según la documentación para las operaciones de creación, obtención, actualización y eliminación.
