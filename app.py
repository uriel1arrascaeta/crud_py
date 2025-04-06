from flask import render_template
from flask import Flask
from flaskext.mysql import MySQL  # conexion a base de datos

app = Flask(__name__)

mysql = MySQL()
# le estamos para que se conecte a la base de datos mysql vamos utilizar localhost
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sistema'
mysql.init_app(app)  # iniciamos


@app.route('/')  # ruta a index
def index():

    sql = "INSERT INTO `empleados` (`id`, `nombre`, `correo`, `foto`) VALUES (NULL, 'oscar', 'perezoscar@gmail.com', 'foto.jpg');"
    conn = mysql.connect()  # conectamos al index con mysql init
    cursor = conn.cursor()  # info donde vamos a guardar todo lo que vamos a ejecutar
    cursor.execute(sql)  # ejecutamos
    conn.commit()  # aca decimos que la instruccion se termino

    return render_template('empleados/index.html')


if __name__ == '__main__':
    app.run(debug=True)
