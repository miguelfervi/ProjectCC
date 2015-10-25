# ProjectCC - Submódulo perteneciente a [PeriodicoInteractivo](https://github.com/ProyectCC/PeriodicoInteractivo)

### Proyecto desarrollado en la asignatura [CC](https://github.com/JJ/clases-CC-2015-16/)




[![Build Status](https://travis-ci.org/JCristobal/ProjectCC.svg?branch=master)](https://travis-ci.org/JCristobal/ProjectCC)

Los intregantes son:

* [José Cristóbal López Zafra](https://github.com/JCristobal)
* [Miguel Fernández Villegas](https://github.com/miguelfervi)
* [Hans Manuel Grenner Noguerón](https://github.com/enpi)
* [Yuan Tian](https://github.com/tianyuan87)



##Integración continua

Para la integración continua usaremos [Travis-CI](https://travis-ci.org/)

Travis provee integración continua hosteada y tiene una integración con GitHub muy sencilla.
Además soporta despliegue para Openshift, Heroku, etc...

Puedes ver el estado actual del proyecto en el *badge* superior o mediante [este enlace](https://travis-ci.org/JCristobal/ProjectCC)


##Test

Los tests los podemos encontrar en test/test.js. Para los tests se han usado las bibliotecas Mocha y Chai.

[Mocha](http://mochajs.org/) es un framework para NodeJS para hacer tests unitarios y [chai](http://chaijs.com/) es una biblioteca de aserciones (assertion library) para NodeJS y para el navegador.


Para instalar mocha, chai y sus plugins:

`sudo npm install mocha --save-dev`
`sudo npm install chai`
`sudo npm install chai-fs`
