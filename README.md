# Submódulo de la aplicación "Periódico interactivo": Análisis y representación de datos

[![Test pasados](https://travis-ci.org/miguelfervi/ProjectCC.svg?branch=master)](https://travis-ci.org/miguelfervi/ProjectCC)


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



