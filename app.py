from flask import Flask,render_template
from flask import request
from src.paquete_principal.principal import Principal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reg')
def registro():
    return render_template('registro.html')

@app.route('/reg_g/<name>',methods = ['POST'])
def registro_g(name):
    principal = Principal()
    id = request.form['id']
    nombre = request.form['nombre']
    clave = request.form['clave']
    email = request.form['email']
    telefono = request.form['telefono']
    persona = principal.fabricaPersona(name,id,nombre,clave,email,telefono)
    return persona.getNombre()

if __name__ == '__main__':
    app.run(port=8080,debug=True)