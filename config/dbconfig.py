from app import app
from flaskext.mysql import MySQL

# DB Config
host = 'localhost'
user = 'user'
password = 'password'
database = 'database'

MySql = MySQL()
app.config['MYSQL_DATABASE_USER'] = user
app.config['MYSQL_DATABASE_PASSWORD'] = password
app.config['MYSQL_DATABASE_DB'] = database
app.config['MYSQL_DATABASE_HOST'] = host
MySql.init_app(app)
