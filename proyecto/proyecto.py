from flask import Flask
from flask import request
from flask import render_template,url_for,session,redirect
import pymongo
import json

app=Flask(__name__)

def cargar():

    with open("proyecto.json") as mi_proyecto:
        proyectos =json.loads(mi_proyecto.read())
        return proyectos

proyectoss=cargar()

conecta= proyectoss['conector'][0]
db= proyectoss['conector'][1]
col= proyectoss['conector'][2]
myclient = pymongo.MongoClient(conecta)
mydb = myclient[db] #Se crea base de datos
mycol = mydb[col]   #Se crea una coleccion = "Tabla"

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/login.html')
def login():

    return render_template("login.html")

@app.route('/registro.html')
def regis():

    return render_template('registro.html')

@app.route('/bienvenida.html')
def bienvenida():

    return render_template("bienvenida.html")

@app.route('/principal.html')
def principal():

    return render_template('principal.html')

@app.route('/login_admin.html')
def login_admin():

    return render_template('login_admin.html')

@app.route('/adminpanel.html')
def adminpanel():

    return render_template('adminpanel.html')

@app.route('/ordenar.html')
def ordenar():

    return render_template('ordenar.html')

@app.route('/cancelados.html')
def cancelados():

    return render_template('cancelados.html')

@app.route('/clientes.html')
def clientes():

    return render_template('clientes.html')

@app.route('/empleados.html')
def empleados():

    return render_template('empleados.html')

@app.route('/finalizados.html')
def finalizados():

    return render_template('finalizados.html')

#inicio de los metodos de los html 

@app.route('/registro', methods = ['POST', 'GET'])
def registro():
    
    nombre=request.form['name']
    apellido=request.form['lastname']
    telefono=request.form['phone']
    contraseña=request.form['password']
    mydict = { "name": nombre, "lastname": apellido, "phone": telefono, "password": contraseña }
    x = mycol.insert_one(mydict)
    print("Registro exitoso Bienvenid@" +nombre+ "a el Maya")
    return "Registro exitoso Bienvenid@: {} a el Maya".format(nombre)






if __name__ == '__main__':
    app.run(debug= True,port= 5000)