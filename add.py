# add.py: Este módulo se ha creado para facilitar la inserción manual de datos en la base de datos.
# Su propósito es demostrar cómo interactuar con el código fuente de la API
# y garantizar que los datos se carguen correctamente en el sistema.
# Aunque en este ejemplo los datos se añaden manualmente,
# este proceso podría automatizarse fácilmente utilizando técnicas como web scraping o integraciones con APIs externas.


# from main import app, db, Cafe
# # Datos de los cafés
# cafes_data = [
#     {
#         "name": "The Break",
#         "location": "Plaza Vía Condotti Entrada principal, Tamarindo 12591 Costa Rica",
#         "phone": "+506 6227 9843",
#         "webpage": "http://www.thebreak.cr/",
#         "reviews": 63,
#         "ranking": "N.º 33 de 247 restaurantes en Tamarindo",
#         "category": "Café",
#         "hours": "Cerrado ahora",
#         "cuisine_types": "Latina, Café, Saludable, Centroamericana, Costarricense",
#         "special_diets": "Opciones vegetarianas, Opciones veganas",
#         "meals": "Desayuno, Comidas, Brunch, Bebidas",
#         "average_rating": 5.0,
#         "advantages": None
#     },
#     {
#         "name": "La Oveja Surf House",
#         "location": "100 meters west of Banco Nacional, Tamarindo 50309 Costa Rica",
#         "phone": "+506 7041 8757",
#         "webpage": "https://www.facebook.com/laovejatama/?locale=sr_RS",
#         "reviews": 864,
#         "ranking": "N.º 2 de 247 restaurantes en Tamarindo",
#         "category": "Café",
#         "hours": "Abierto ahora 7:00 - 0:00",
#         "cuisine_types": "Bar, Café, Contemporánea, Fusión, Saludable",
#         "special_diets": "Opciones vegetarianas",
#         "meals": "Desayuno, Comidas, Cenas, Brunch, Bebidas",
#         "average_rating": 5.0,
#         "advantages": None
#     },
#     {
#         "name": "Flora Vegan Cafe",
#         "location": "8526+W3J C. Sunrise Tamarindo, Tamarindo 50309 Costa Rica",
#         "phone": "+506 6306 5870",
#         "webpage": "http://www.floravegancafe.com/",
#         "reviews": 56,
#         "ranking": "N.º 1 de 13 cafeterías y teterías en Tamarindo",
#         "category": "Café",
#         "hours": "Abierto ahora 8:30 - 18:00",
#         "cuisine_types": "Café, Tienda gourmet, Contemporánea, Saludable",
#         "special_diets": "Opciones vegetarianas, Opciones veganas",
#         "meals": None,
#         "average_rating": 5.0,
#         "advantages": None
#     },
#     {
#         "name": "Breaking Bread",
#         "location": "Centro Comercial el Punto, local 10 a 40m Oeste Del Supercompro, Tamarindo Costa Rica",
#         "phone": "+506 8679 2809",
#         "webpage": "http://www.facebook.com/pages/category/Bakery/Breaking-bread-tamarindo-199399737437913",
#         "reviews": 391,
#         "ranking": "N.º 1 de 3 panaderías en Tamarindo",
#         "category": "Café",
#         "hours": "Abierto ahora 6:00 - 15:00",
#         "cuisine_types": "Café, Saludable",
#         "special_diets": "Opciones vegetarianas, Opciones veganas, Opciones sin gluten",
#         "meals": "Desayuno, Comidas, Brunch",
#         "average_rating": 5.0,
#         "advantages": None
#     },
#     {
#         "name": "Cafe Santa Rita",
#         "location": "Complejo Sunrise Plaza Local Nro 15, Tamarindo Costa Rica",
#         "phone": "+506 4034 0501",
#         "webpage": "https://www.facebook.com/773323146083430",
#         "reviews": 400,
#         "ranking": "N.º 14 de 247 restaurantes en Tamarindo",
#         "category": "Café",
#         "hours": "Abierto ahora 8:00 - 15:30",
#         "cuisine_types": "Café, Internacional, Saludable, Costarricense",
#         "special_diets": "Opciones vegetarianas, Opciones sin gluten",
#         "meals": "Desayuno, Comidas, Brunch, Bebidas",
#         "average_rating": 5.0,
#         "advantages": None
#     },
#     {
#         "name": "Pots & Bowls Playa Grande",
#         "location": "100 metros oeste de la asada de playa grande Local Right Hand, Playa Grande 50308 Costa Rica",
#         "phone": "+506 8492 5051",
#         "webpage": "http://www.potsandbowlscr.com/",
#         "reviews": 207,
#         "ranking": "N.º 1 de 25 restaurantes en Playa Grande",
#         "category": "Café",
#         "hours": "Abierto ahora 7:30 - 20:00",
#         "cuisine_types": "Café, Saludable, Centroamericana, Costarricense",
#         "special_diets": "Opciones vegetarianas, Opciones veganas, Opciones sin gluten",
#         "meals": "Desayuno, Comidas, Cenas, Brunch, Bebidas",
#         "average_rating": 5.0,
#         "advantages": None
#     }
# ]
#
# # Agregar cafés a la base de datos
# with app.app_context():
#     # Eliminar todos los cafés existentes
#     db.session.query(Cafe).delete()  # Elimina todos los cafés existentes
#     # Agregar los nuevos cafés
#     for cafe in cafes_data:
#         new_cafe = Cafe(
#             name=cafe["name"],
#             location=cafe["location"],
#             phone=cafe["phone"],
#             webpage=cafe["webpage"],
#             reviews=cafe["reviews"],
#             ranking=cafe["ranking"],
#             category=cafe["category"],
#             hours=cafe["hours"],
#             cuisine_types=cafe["cuisine_types"],
#             special_diets=cafe["special_diets"],
#             meals=cafe["meals"],
#             average_rating=cafe["average_rating"],
#             advantages=cafe["advantages"]
#         )
#         db.session.add(new_cafe)  # Agregar a la sesión
#     db.session.commit()  # Guardar los cambios
