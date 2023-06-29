######################################
# Nombre:  Raul Hernandez Lopez @Neo #
# Email:    freeenergy1975@gmail.com #
# fecha: domingo 5 de junio del 2022 #
######################################

############bibliotecas####################
from flask import Flask, jsonify, request #
from flask_sqlalchemy  import  SQLAlchemy #
from flask_marshmallow import Marshmallow #
from flask_cors import CORS, cross_origin #
from datetime import datetime             #
from sqlalchemy.sql import func           #
###########################################
from Conexion import conexion as cn

##################################Creadenciales de la base de datos#########################################
app = Flask(__name__)   
app.config['SQLALCHEMY_DATABASE_URI'] = cn.cadena_conexion

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
##################################Origenes cruzados#########################################################
CORS (app)
CORS (app, resources={
    r"/*":{
    "origins":"*"
    }})

db = SQLAlchemy(app)
ma = Marshmallow(app)

########################### Creacion de la tabla usuario ###################################################
class Usuario(db.Model):
        clv_usuario = db.Column(db.String(5), primary_key = True)
        nombre_usuario = db.Column(db.String(30), unique=True, nullable = False)
        contrasenia_usuario = db.Column(db.String(30), nullable = False)
        tipo_usuario = db.Column(db.String(15), nullable = False)

        def __init__(self, clv_usuario, nombre_usuario, contrasenia_usuario, tipo_usuario):
                self.clv_usuario = clv_usuario
                self.nombre_usuario = nombre_usuario
                self.contrasenia_usuario = contrasenia_usuario
                self.tipo_usuario = tipo_usuario

with app.app_context():
    db.create_all()
#########################   Creacion de la tabla encuesta de satisfaccion ##################################
class EncuestaSatisfaccion(db.Model):
    id_encuesta = db.Column(db.Integer(), autoincrement=True, primary_key=True)
    nivel_satisfaccion = db.Column(db.Integer, nullable = False)
    comentario = db.Column(db.Text)
    folio = db.Column(db.String(18))
    fecha = db.Column(db.DateTime, default=datetime.now)
    # Tanto el id y el campo de fecha son automaticos por lo que no especifican en la funcion init
    def __init__(self, nivel_satisfaccion, comentario, folio):
        self.nivel_satisfaccion = nivel_satisfaccion
        self.comentario = comentario
        self.folio = folio


with app.app_context():
    db.create_all()
################################## Creacion de esquemas #####################################################
class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('clv_usuario', 'nombre_usuario', 'contrasenia_usuario', 'tipo_usuario')

#Devuelve  los resgistros de un  usuario.
usuarioSchema = UsuarioSchema()
#Devuelve todos lo registros de usuarios.
usuarioSchemas = UsuarioSchema(many=True)

class EncuestaSchema(ma.Schema) :
    class Meta:
        fields = ('id_encuesta', 'nivel_satisfaccion', 'comentario', 'folio', 'fecha')

#Devuelve los registros de una encuesta
encuestaSchema = EncuestaSchema()
#Devuelve todos los resgistros de la encuesta
encuestasSchemas = EncuestaSchema(many=True)

#########################################  Metodos web #######################################################GET USUARIOS
@app.route('/usuario', methods=['GET'])
def obtenerUsuarios():
    todos_los_usuarios = Usuario.query.all()
    consulta_usuarios = usuarioSchemas.dump(todos_los_usuarios)
    return jsonify(consulta_usuarios)

#GET USUARIO
@app.route('/usuario/<name>', methods=['GET'])
def obtenerUsuario(name):
    un_usuario = Usuario.query.filter_by(nombre_usuario=name).first()
    return usuarioSchema.jsonify(un_usuario)

#GET ENCUESTAS
@app.route('/encuesta', methods=['GET'])
def obtenerEncuestas():
    todas_las_encuestas = EncuestaSatisfaccion.query.all()
    consulta_encuestas = encuestasSchemas.dump(todas_las_encuestas)
    return jsonify(consulta_encuestas)

#POST
@app.route('/usuario/nuevo_usuario', methods=['POST'])
def insertar_usuario():
    datosJSON = request.get_json(force=True)

    clv_usuario = datosJSON ['clv_usuario']
    nombre_usuario = datosJSON ['nombre_usuario']
    contrasenia_usuario = datosJSON ['contrasenia_usuario']
    tipo_usuario = datosJSON ['tipo_usuario']

    nuevo_usuario = Usuario(clv_usuario, nombre_usuario, contrasenia_usuario, tipo_usuario)

    db.session.add(nuevo_usuario)
    db.session.commit()
    return usuarioSchema.jsonify(nuevo_usuario)

#POST
@app.route('/nivel_satifaccion/nuevo_nivel_satifaccion', methods=['POST'])
def insertar_nivel_satisfaccion():
    datosJSON = request.get_json(force=True)

    nivel_satisfaccion =  datosJSON['nivel_satisfaccion']
    comentario = datosJSON['comentario']
    folio = datosJSON['folio']


    nuevo_nivel_satisfaccion = EncuestaSatisfaccion(nivel_satisfaccion, comentario, folio)

    db.session.add(nuevo_nivel_satisfaccion)
    db.session.commit()
    return encuestaSchema.jsonify(nuevo_nivel_satisfaccion)

#PUT
@app.route('/usuario/actualizar_usuario/<clv>', methods=['PUT'])
def actualizarUsuario(clv):
    actualizar_usuario = Usuario.query.get(clv)

    datosJSON = request.get_json(force=True)
    nombre_usuario = datosJSON['nombre_usuario']
    contrasenia_usuario = datosJSON['contrasenia_usuario']
    tipo_usuario = datosJSON['tipo_usuario']

    actualizar_usuario.nombre_usuario = nombre_usuario
    actualizar_usuario.contrasenia_usuario = contrasenia_usuario
    actualizar_usuario.tipo_usuario = tipo_usuario

    db.session.commit()
    return usuarioSchema.jsonify(actualizar_usuario)

#DELETE
@app.route('/usuario/eliminar_usuario/<clv>', methods=['DELETE'])
def eliminarUsuario(clv):
    eliminar_usuario = Usuario.query.get(clv)

    db.session.delete(eliminar_usuario)
    db.session.commit()

    return usuarioSchema.jsonify(eliminar_usuario)

if __name__=="__main__":
    #En este apartado se especifica la ruta del servidor
    app.run(debug=True, port="4040", host="192.168.124.90")
