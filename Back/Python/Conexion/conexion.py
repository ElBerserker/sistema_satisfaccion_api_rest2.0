######################################
# Nombre:  Raul Hernandez Lopez @Neo #
# Email:    freeenergy1975@gmail.com #
# fecha: sabado 10 de junio del 2023 #
######################################

# Configuración de la conexión a la base de datos
host = 'www.lynx.model'
db = 'sistema_satisfaccion'
user = 'Berserker_db'
passwd = 'db_maria1.1'

# Crea una cadena de conexión para MariaDB
cadena_conexion = 'mysql+pymysql://'+ user +':'+ passwd + '@' + host + '/' + db
