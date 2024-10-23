
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text, Float
from pydantic import BaseModel
from typing import List, Optional
import random

app = Flask(__name__)

# Configuración de la base de datos
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/stevenmendez/Desktop/Api_restfull/Api_restfull_python/instance/cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# Definición del modelo de datos
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    location: Mapped[str] = mapped_column(String(500), nullable=False)
    phone: Mapped[str] = mapped_column(String(50), nullable=False)
    webpage: Mapped[str] = mapped_column(String(500), nullable=True)
    reviews: Mapped[int] = mapped_column(Integer, nullable=False)
    ranking: Mapped[str] = mapped_column(String(250), nullable=False)
    category: Mapped[str] = mapped_column(Text, nullable=False)  # Cambiado a Text para listas
    hours: Mapped[str] = mapped_column(String(100), nullable=False)
    cuisine_types: Mapped[str] = mapped_column(Text, nullable=False)  # Cambiado a Text para listas
    special_diets: Mapped[str] = mapped_column(Text, nullable=True)  # Cambiado a Text para listas
    meals: Mapped[str] = mapped_column(Text, nullable=True)  # Cambiado a Text para listas
    average_rating: Mapped[float] = mapped_column(Float, nullable=False)  # Cambiado a Float para ratings
    advantages: Mapped[str] = mapped_column(Text, nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()

# Esquema de validación
class CafeModel(BaseModel):
    id: int
    name: str
    location: str
    phone: str
    webpage: Optional[str] = None
    reviews: int
    ranking: str
    category: str
    hours: str
    cuisine_types: str
    special_diets: Optional[str] = None
    meals: Optional[str] = None
    average_rating: float
    advantages: Optional[str] = None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafes", methods=["GET"])
def get_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])


@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.json
    new_cafe = Cafe(
        name=data['name'],
        location=data['location'],
        phone=data['phone'],
        webpage=data.get('webpage'),
        reviews=data['reviews'],
        ranking=data['ranking'],
        category=data['category'],
        hours=data['hours'],
        cuisine_types=data['cuisine_types'],
        special_diets=data.get('special_diets'),
        meals=data.get('meals'),
        average_rating=data['average_rating'],
        advantages=data.get('advantages')
    )
    db.session.add(new_cafe)
    db.session.commit()

    # Agregar la respuesta del ID
    return jsonify({"message":"Café agregado exitosamente.", "id":new_cafe.id}), 201


@app.route("/search", methods=["GET"])
def search_cafes():
    location = request.args.get("loc")  # Obtener el parámetro de ubicación de la consulta
    if not location:
        return jsonify({"error": "Ubicación no proporcionada"}), 400  # Manejo de error si no hay ubicación

    # Filtrar los cafés por ubicación
    result = db.session.execute(db.select(Cafe).filter(Cafe.location.ilike(f'%{location}%')))
    cafes = result.scalars().all()  # Obtener los cafés que coinciden

    if cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in cafes])  # Devolver cafés encontrados
    else:
        return jsonify({"message": "No se encontraron cafés en esa ubicación."}), 404  # Manejo de error si no hay cafés



@app.route("/update/<int:id>", methods=["PUT"])
def update_cafe(id):
    cafe = db.session.get(Cafe, id)
    if not cafe:
        return jsonify({"message": "Café no encontrado."}), 404

    data = request.json
    cafe.ranking = data.get('ranking', cafe.ranking)
    cafe.average_rating = data.get('average_rating', cafe.average_rating)

    db.session.commit()
    return jsonify({"message": "Café actualizado exitosamente."})

@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_cafe(id):
    cafe = db.session.get(Cafe, id)
    if not cafe:
        return jsonify({"message": "Café no encontrado."}), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify({"message": "Café eliminado exitosamente."})

@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    if not cafes:
        return jsonify({"message": "No hay cafés disponibles."}), 404
    random_cafe = random.choice(cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)




