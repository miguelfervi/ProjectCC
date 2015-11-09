var assert = require('assert');

var chai = require('chai');//Añado mocha
var expect = chai.expect;
chai.use(require('chai-fs'));

var request = require('supertest');//Biblioteca para comprobar servidores web
var urlServidor = "http://localhost:8080";//URL del servidor donde se ejecuta la aplicación
var urlServidorGraficos = "http://localhost:8080/highchart";//Url de la parte de gráficas

describe('Test basicos', function() {




  describe('Comprobando  archivos', function () {

    it('El fichero script existe', function (done) {
      expect('script.py').to.be.a.file();
      done();
    });

    it('Archivos de documentación "pycco"', function (done) {
      expect('docs/script.html').to.be.a.file();
      expect('docs/pycco.css').to.be.a.file();
      done();
    });

  });


/*  describe('Pruebas de accesibilidad', function () {

   
   it('Comprobando que el servidor está encendido', function (done) {
      request(urlServidor).get('/').expect(200).end(function(err, res){
      if (err)
        return done(err)
        done();
      });
    });
    
    it('Comprobando que generamos las gráficas por medio de HighChart', function (done) {
      request(urlServidorGraficos).get('/').expect(200).end(function(err, res){
      if (err)
        return done(err)
        done();
      });
    });


  })*/



});

