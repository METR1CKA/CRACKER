# CRACKER

Script hecho en `python` para decifrar contraseñas encriptadas en `MD5`

# Requisitos

* Python

# Instrucciones

1. Ejecutar el archivo `main.py`

~~~bash

python3 main.py

~~~

2. Ingresar la contraseña hasheada en `MD5` y el path del diccionario de contraseñas

~~~bash

[+] Enter the MD5 hashed password: 0192023a7bbd73250516f069df18b500

[+] Enter the dictionary path: $PATH/dictionary.txt

~~~

3. Espere su resultado

~~~bash

[*] Results: admin123

~~~

## Otras respuestas

* En caso de que no encontrar el archivo

~~~bash

[*] Results: [Errno 2] No such file or directory: '$PATH'

~~~

* En caso de no encontrar match en las respuestas

~~~bash

[*] Results: Password not found

~~~

## Nota

> El proyecto incluye un archivo `.txt` con algunas contraseñas, puedes incluir mas si gustas y en caso de que lo requieras

# **METR1CKA**

> [Visitanos en DevBlogs](https://metr1cka.github.io "Pagina web")

> [Mas repositorios](https://github.com/METR1CKA "Mi perfil")
