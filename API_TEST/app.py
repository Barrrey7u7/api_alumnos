from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuración de la base de datos PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cruddb_vo91_user:Bgmktg1nlxHW3FUmj7o2YluLS0Xd94kx@dpg-cups8s5svqrc73f5bnq0-a.oregon-postgres.render.com/cruddb_vo91'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Definición del modelo de la tabla 'alumnos'
class Alumno(db.Model):
    __tablename__ = 'alumnos'
    no_control = db.Column(db.String, primary_key=True)
    nombre = db.Column(db.String, nullable=True)
    ap_paterno = db.Column(db.String, nullable=True)
    ap_materno = db.Column(db.String, nullable=True)
    semestre = db.Column(db.Integer, nullable=True)

# Endpoint para obtener todos los alumnos


# Endpoint para agregar un nuevo alumno
@app.route('/alumnos', methods=['POST'])
def agregar_alumno():
    data = request.get_json()
    nuevo_alumno = Alumno(
        no_control=data['no_control'],
        nombre=data['nombre'],
        ap_paterno=data['ap_paterno'],
        ap_materno=data['ap_materno'],
        semestre=data['semestre']
    )
    db.session.add(nuevo_alumno)
    db.session.commit()
    return jsonify({'mensaje': 'Alumno agregado exitosamente'}), 201


# Endpoint para obtener un alumno por no_control


# Endpoint para actualizar un alumno


# Endpoint para eliminar un alumno


if __name__ == '__main__':
    app.run(debug=True)