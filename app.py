from flask import render_template
from flask import Flask
from flaskext.mysql import MySQL  # conexion a base de datos

app = Flask(__name__)


@app.route('/')  # ruta a index
def index():
    return render_template('empleados/index.html')


if __name__ == '__main__':
    app.run(debug=True)
