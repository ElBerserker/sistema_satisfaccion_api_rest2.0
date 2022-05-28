from flask import Flask, request, jsonify
from flask_sqlalchemy  import  SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
#Credenciales de la base de datos.
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Berserker_db:db_maria1.1@192.168.1.71:3306/Prueba'
app.config['SQLALCHEMY_TRACK_MOFIDICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)


########################################################################################
#Creacion de la tabla en la base de datos
class User(db.Model):
	id_user = db.Column(db.String(5), primary_key = True)
	name_user = db.Column(db.String(30), unique=True)
	password_user = db.Column(db.String(30))
	type_user = db.Column(db.String(15))
	
	def __init__(self, id_user, name_user, password_user, type_user):
		self.id_user = id_user
		self.name_user = name_user
		self.password_user = password_user
		self.type_user = type_user
		
db.create_all()

class UserSchema(ma.Schema):
	class Meta:
		fields = ('id_user', 'name_user', 'password_user', 'type_user')
		
#Una sola respuesta.
user_schema = UserSchema()
#Varias respuestas.
users_schemas = UserSchema(many=True)
#######################################################################################		
@app.route('/user', method=['GET'])
def get_users():
	all_users = User.query.all()
	result_query_users = user_schema.dump(all_users)
	return jsonify(result_query_users)
	

@app.route('/', methods=['GET'])
def index():
	return jsonify({'mensaje : hola'})
	
			
if __name__=="main":
	app.run(debug=True)
	
	
	
