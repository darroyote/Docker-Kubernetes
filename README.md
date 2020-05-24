# Proyecto


La aplicación esta realizada en Flask y mediante variables de conexión del mysql conecta a dicho contenedor.Una vez esta los dos contenedores running y conectados, verificaremos mediante: http://localhost:8080 que podemos agregar y borrar contenido en nuestra lista

## REQUISITOS

Para hacer que funcione necesitaremos tener docker instalado.
Con los contenedores cargaran SO, flask, python, ysql y dependencias necesarias para que se ejecuten de forma correcta, pero sin modificar, ni instalar nada en el anfitrión

Para su creación es necesario:
  - Tener cuenta en GITHUB para subir el código y instrucciones
  - Tener cuenta en docker paras subir las imagenes y poder descargártelas desde cualquier ordenador
  - Instalar/configurar Kubernetes (KUBEADM, KUBECTL)
  - Instalar/configurar Helm
En esta práctica, el clutser de Kubernetes se ha instalado en una EC2.


## ESTRUCTURA

La estructura que puedes encontrar en el proyecto se compone de la siguiente carpetas:

  - mysql : Obtenemos el dockerfile (con variables de entorno) y ficheros que necesita el sql para ejecutarse de forma correcta. 
  Imagen en docker: darroyote/mysql_for_rtb:v1 
  - rtbm : Aplicación flask, qe conectará con al BBDD y nos permitirá realizar una lista. También veremos su dockerfile con las variables de entorno. 
  Imagen en docker: darroyote/myrtb:v1

## EJECUCIÓN

  - Crear contenedor mysql: (la nombramos mysql)
    ```
    sudo docker run --name mysql darroyote/mysql_for_rtb:v1
    ```
  - Crear contenedor app: (lincamos con la BBDD)
    ```
    docker run -p 8080:8080 --link mysql:mysql darroyote/myrtb:v1
    ```
  - Accedemos a: http://localhost:8080 Si estamos en una ec2, veremos la ip pública de la máquina      


## PENDIENTE -- TENGO FICHEROS CREADOS, PERO SIN FUNCIONAR (manifiesto Kubernetes y chart de helm a colgar mas adelante)
  ##### KUBERNETES 
  Versión  
  ```
  ubuntu@:~$ kubectl version
  Client Version: version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.2",      GitCommit:"52c56ce7a8272c798dbc29846288d7cd9fbae032", GitTreeState:"clean", BuildDate:"2020-04-16T11:56:40Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}
  Server Version: version.Info{Major:"1", Minor:"18", GitVersion:"v1.18.2", GitCommit:"52c56ce7a8272c798dbc29846288d7cd9fbae032", GitTreeState:"clean", BuildDate:"2020-04-16T11:48:36Z", GoVersion:"go1.13.9", Compiler:"gc", Platform:"linux/amd64"}
  ```
  Cluster Kubernetes instalado
  ```
  ubuntu@ip:~$ kubectl get nodes  
  NAME            STATUS   ROLES    AGE   VERSION  
  ip-10-0-1-176   Ready    <none>   13d   v1.18.2  
  ip-10-0-1-59    Ready    master   13d   v1.18.2
  ```
  ##### HELM
  ```
  ubuntu@ip:~$ helm version
  version.BuildInfo{Version:"v3.2.1", GitCommit:"fe51cd1e31e6a202cba7dead9552a6d418ded79a", GitTreeState:"clean",       GoVersion:"go1.13.10"}
   ```
  ## BÚSQUEDA DE INFORMACIÓN
  
  https://docs.docker.com/get-docker/
  https://stackoverflow.com/

