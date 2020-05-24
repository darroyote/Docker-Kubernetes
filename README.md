Proyecto

La aplicación esta realizada en Flask y mediante variables de conexión del mysql conecta a dicho contenedor.Una vez esta los dos contenedores running y conectados, verificaremos mediante: http://localhost:8080 que podemos agregar y borrar contenido en nuestra lista

Para hacer que funcione necesitaremos tener docker instalado.

La estructura que puedes encontrar en el proyecto se compone de la siguiente carpetas:

  - mysql : Obtenemos el dockerfile (con variables de entorno) y ficheros que necesita el sql para ejecutarse de forma correcta.
  - rtbm : Aplicación flask, qe conectará con al BBDD y nos permitirá realizar una lista. También veremos su dockerfile con las variables de entorno

Ejecución:

  - Crear contenedor mysql: (la nombramos mysql)
      docker run -d --name mysql darroyote/mysql_for_rtb:v1
  
  - Crear contenedor app: (lincamos con la BBDD)
      docker run -p 8080:8080 --link mysql:mysql darroyote/myrtb:v1
  
  - Accedemos a: http://localhost:8080 Si estamos en una ec2, veremos la ip pública de la máquina      

Otra manera de ejecutarlo será ejecutando docker-compose up del fichero llamado "docker-compose.yml
