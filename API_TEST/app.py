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


# Endpoint para obtener un alumno por no_control
@app.route('/alumnos/<no_control>', methods=['GET'])
def obtener_alumno(no_control):
    alumno = Alumno.query.get(no_control)
    if alumno is None:
        return jsonify({'mensaje': 'Alumno no encontrado'}), 404
    return jsonify({
        'no_control': alumno.no_control,
        'nombre': alumno.nombre,
        'ap_paterno': alumno.ap_paterno,
        'ap_materno': alumno.ap_materno,
        'semestre': alumno.semestre
    })


# Endpoint para actualizar un alumno



# Endpoint para eliminar un alumno
@app.route('/alumnos/<no_control>', methods=['DELETE'])
def eliminar_alumno(no_control):
    alumno = Alumno.query.get(no_control)
    if alumno is None:
        return jsonify({'mensaje': 'Alumno no encontrado'}), 404
    db.session.delete(alumno)
    db.session.commit()
    return jsonify({'mensaje': 'Alumno eliminado exitosamente'})

if __name__ == '__main__':
    app.run(debug=True)