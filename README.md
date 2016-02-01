# Submódulo de la aplicación "Periódico interactivo": Análisis y representación de datos

[![Test pasados](https://travis-ci.org/miguelfervi/ProjectCC.svg?branch=master)](https://travis-ci.org/miguelfervi/ProjectCC)
[![Heroku Status](https://heroku-badge.herokuapp.com/?app=periodicointeractivo&style=flat)](https://periodicointeractivo-modudato.herokuapp.com/)

#Práctica 1

Este submódulo es el correspondiente a la gestión de análisis de datos y estadisticas, para mejorar la aplicación y analizar tanto posibles irregularidades como mejora de la aplicación a través de datos númericos.

Este súbmodulo está bajo la licencia [GNU GENERAL PUBLIC LICENSE](https://github.com/miguelfervi/ProjectCC/blob/master/LICENSE) y será realizado por [Miguel Fernández Villegas](https://github.com/miguelfervi)

Este módulo llevará a cabo presentación de la información que el usuario necesite, para ofrecer esta información de una forma más amigable se generarán gráficas interactivas para mostrar los datos analizados. Estos datos pasarán por un proceso estadístico, en el que estudiaremos los datos obtenidos en nuestro análisis de datos.

Para hacer el análisis de datos vamos a usar el lenguaje de programación R, y librerías de python para este propósito específico, de forma que podamos refinar los datos que sean interesantes en el sitio web.

Usaré una librería para python que nos permite integrar R: [Rpy2](http://rpy.sourceforge.net/), esta librería permite introducir operaciones en R e integrarlas en Python.

Para mostrar los resultados, voy a usar [Highcharts](http://www.highcharts.com/), una API libre para añadir a nuestros sitios web, gráficas para mostrar todo tipo de información y recolección de datos de forma que representemos gráficamente el trabajo realizado en R.


##Motivación

El mundo contiene millones de datos, algo necesario en nuestra sociedad aunque a veces, no sea lo más deseable. Nuestro sitio web debe tener este módulo para poder analizar el tipo de usuarios que tenemos y adaptarnos a sus posibles necesidades en un futuro a medio/largo plazo.

##Objetivos a alcanzar

El fin de este módulo es conseguir representar, gran cantidad de información, en la que se puede desechar y explotar datos concretos en la recolección los mismos, de una forma más correcta y sobre todo más visible para todos los usuarios y este submódulo se integrará en el [proyecto principal](https://github.com/ProyectCC/PeriodicoInteractivo).

#Práctica 2
##Integración continua

Para la integración continua usaremos [Travis-CI](https://travis-ci.org).

Travis nos proporciona integración continua y con Github es realmente fácil su uso.

La configuración se realiza a partir del fichero .travis.yml en el directorio principal de nuestro repo. En este archivo añadimos, las versiones del lenguaje de programación usado, probar los test e instalar las dependencias.

Puedes ver el estado actual del proyecto en el badge Build Status o accediendo a la página web generada con las resultados de integración de nuestro proyecto.

El proceso que se sigue es el siguiente:

Se hace un push en el proyecto
Github envía una petición a Travis para que realice un nuevo build.
Travis toma nuestro .travis.yml e instala las dependencias necesarias y checkea las versiones distintas del lenguaje usado

Se ejecutan los test. Si todo va correctamente nuestro badge se pondrá de color verde, y así podemos exportarlo, por ejemplo al principio de este archivo, la prueba de que nuestro repo se ha podido integrar de forma correcta.

##Test

Para la realización de los test hemos usado un framework para realizar test que corre en Node.js, llamado Mocha, también hosteados en Github, pero no será la única herramienta usada, ya que añadiremos también Chai y Supertest.

Chai es una biblioteca de aserciones para NodeJS y para el navegador, que integraremos con Mocha. Chai nos ayuda a realizar aserciones contra nuestro código. 

Supertest es otra librería para hacer aserciones HTTP. Permite hacer pruebas HTTP de alto nivel y así poder compobar el funcionamiento de nuestro servidor. Los test con Supertest los haremos sólo en local, ya que no podemos desplegar el servidor en Travis para que realice los test.

Los tests los podemos encontrar en test/test.js. Para realizarlos ejecutamos npm test.

Para instalar Mocha y las distintas librerias:

`sudo npm install mocha --save-dev`

`sudo npm install chai`

`sudo npm install chai-fs `

`sudo npm install supertest`


El procedimiento una vez instalado y preparado todo lo necesario para realizar los test es:

Creamos el directorio [test](https://github.com/miguelfervi/ProjectCC/tree/master/test)
y creamos el archivo [test.js](https://github.com/miguelfervi/ProjectCC/blob/master/test/test.js), después volvemos al directorio raíz y ejecutamos la siguiente orden, `npm test`y ya los test serán mostrando el éxito o fallo que pueda producirse.

#Práctica 3


##Plataforma como servicio (Paas): Heroku


[Heroku](https://www.heroku.com/platform) es una plataforma como servicio ("Platform as a Service" o PaaS) de computación en la nube que soporta distintos lenguajes de programación, Python, en concreto, que es el que usamos, por tanto, me he decidido a usarlo como Paas para nuestra aplicación.

Plataforma con gran cantidad de características, aunque solo mencionaré algunas de ellas.

* [X] Despliegue instanteneo realizado con Git push, la Build por Heroku es realizada por tus build script
* [X] Gran cantidad de Add-on de recursos como pueden ser: aplicaciones, bases de datos, entre otros
* [X] Escalado de procesos, cada componente de la aplicación se trata independientemente sin afectar a la funcionalidad y el rendimiento del resto.
* [X] Aislamiento, cada proceso (nombrado dyno o contenedor) está completamente aislado de otro


Heroku te permite tener 5 contenedores gratuitos en tu cuenta sin ningún tipo de coste adicional. También permite conectarse con GitHub, lo que facilita tener el Paas siempre actualizado a nuestra versión de GitHub.

Algunos de sus competidores son los siguientes:

[AWS Elastic Beanstalk](https://aws.amazon.com/es/)

[Bluemix](https://console.ng.bluemix.net/)

[Google App Engine](https://cloud.google.com/appengine/docs)

[OpenShift](https://www.openshift.com/)

[Windows Azure](https://azure.microsoft.com/es-es/)

A continuación se va a realizar un pequeño tutorial sobre la creación y el despliegue en Heroku.
Para empezar debemos situarnos en el directorio de nuestro proyecto e instalar [toolbelt](https://toolbelt.heroku.com/) en caso de no tenerlo.

Después creamos en nuestra consola de comandos nuestro proyecto en Heroku 
`heroku apps:create --region eu --buildpack heroku/python periodicointeractivo-modudato` el modudato es para que no produzca conflictos con el resto de mi equipo de trabajo y para señalar que es mi parte del submódulo.

Tambiién asignamos el puerto 8080 para usarlo al desplegar la aplicación
`heroku config:set PORT=8080`

Y por último guardamos los cambios con git. En el caso de Heroku con
`git push heroku master`, pero nosotros antes pasaremos por Travis y después si todo es correcto desplegaremos la aplicación.

Como se puede observar [aquí](https://gyazo.com/7c7bec97c6184d7f658c1e2030190bf3.png) el PaaS está asociado y configurado con GitHub. También hemos activado la opción de que para desplegarse, deberá haber pasado con éxito los test en CI.
En el momento que cambiemos algo del repositorio y lo subamos a GitHub, pasa por Travis CI y si el resultado tiene éxito lo despliega en Heroku, en el caso de que Travis falle, no se desplegará en Heroku.

Por último aquí se adjunta una captura de como ha sido [desplegada una vez finalizado](https://gyazo.com/edfe5b2c38a23da46edac725d1090614.png) la aplicación y por último el enlace de la aplicación desplegada.
[Enlace a la aplicación en Heroku](https://periodicointeractivo-modudato.herokuapp.com/)


#Práctica 4

##Entorno de pruebas mediante contenedores Docker

Antes de desplegarse a producción, las aplicaciones tendrá que probarse en un entorno aislado. Para ello se usa Docker, creando un entorno de pruebas para la aplicación. Además se descarga y se deja preaparado para el despliegue de la aplicación (sólo con ejecutar python home/PeriodicoInteractivo/script.py). El contenedor está disponible en [DockerHub](https://hub.docker.com/r/miguelfervi/ubuntu-periodicointeractivo/), enlazado a un [repositorio](https://github.com/miguelfervi/ubuntu-PeriodicoInteractivo) que actualizará el contenedor cada vez que se realicen cambios. Para descargarlo simplemente habrá que ejecutar:

sudo docker pull miguelfervi/ubuntu-periodicointeractivo

y para desplegarlo:

`sudo docker run -t -i miguelfervi/ubuntu-periodicointeractivo`

Imagen del contenedor descargado y desplegado: 



