# ProjectCC - Submódulo perteneciente a [PeriodicoInteractivo](https://github.com/ProyectCC/PeriodicoInteractivo)

### Proyecto desarrollado en la asignatura [CC](https://github.com/JJ/clases-CC-2015-16/)




[![Build Status](https://travis-ci.org/JCristobal/ProjectCC.svg?branch=master)](https://travis-ci.org/JCristobal/ProjectCC)

Responsable del módulo: [José Cristóbal López Zafra](https://github.com/JCristobal).



##Documentación pycco

Usaré [pycco](http://fitzgen.github.io/pycco/), "versión python de Docco".

Una vez instalado con `sudo pip install pycco` ejecuto `pycco script.py` o `pycco *.py` si hay varios archivos python.

Los documentos generados (html con sus respectivos css) los puedo ver en el directorio [docs/](https://github.com/JCristobal/ProjectCC/tree/master/docs) 



##Integración continua

Para la integración continua usaremos [Travis-CI](https://travis-ci.org/).

Travis provee integración continua hosteada y tiene una integración con GitHub muy sencilla.
Además soporta despliegue para Openshift, Heroku, etc...

Puedes ver el estado actual del proyecto en el *badge* superior o mediante [este enlace](https://travis-ci.org/JCristobal/ProjectCC).


##Test

Los tests los podemos encontrar en [test/test.js](https://github.com/JCristobal/ProjectCC/blob/master/test/test.js). Para los tests se han usado las bibliotecas Mocha y Chai.

[Mocha](http://mochajs.org/) es un framework para NodeJS para hacer tests unitarios y [Chai](http://chaijs.com/) es una biblioteca de aserciones (assertion library) para NodeJS y para el navegador.


Para instalar Mocha, Chai y sus plugins:

`sudo npm install mocha --save-dev`
`sudo npm install chai`
`sudo npm install chai-fs`
