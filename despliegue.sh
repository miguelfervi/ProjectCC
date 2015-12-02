#!/bin/bash

# Tendremos que tener Git instalado y con las variables correctamente instaladas
# apt-get install git
git clone https://github.com/miguelfervi/ProjectCC

cd ProjectCC

# El toolbelt de Heroku debe estar instalado y configurado
# wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
# heroku login
heroku apps:create --region eu --buildpack heroku/python periodicointeractivo-modulodato

#echo "web: python script.py $PORT" > Procfile # No hace falta, se incluye en el repo

# Declaramos variables internas de Heroku
heroku config:set PORT=8080

# Desplegamos la aplicación a Heroku
git push heroku master

# Abrimos el navegador con la aplicación
heroku open
