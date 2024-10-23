import unittest
from main import app, db, Cafe
import random

class CafeAPITestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_cafes.db'  # Cambia aquí
        self.app = app
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_cafes(self):
        response = self.client.get('/cafes')
        self.assertEqual(response.status_code, 200)
        self.assertIn('cafes', response.get_data(as_text=True))

    def test_add_cafe(self):
        cafe_data = {
            "name": "Café Test",
            "location": "Ubicación Test",
            "phone": "123456789",
            "webpage": "http://example.com",
            "reviews": 10,
            "ranking": "5 estrellas",
            "category": "Café",
            "hours": "8 AM - 8 PM",
            "cuisine_types": "Café",
            "special_diets": "Ninguno",
            "meals": "Desayuno",
            "average_rating": 4.5,
            "advantages": "Buena atención"
        }

        response = self.client.post('/add', json=cafe_data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('Café agregado exitosamente.', response.get_json()['message'])

        # Verificar que el café se ha añadido
        response = self.client.get('/cafes')
        self.assertEqual(response.status_code, 200)
        cafes = response.get_json()['cafes']
        self.assertTrue(any(cafe['name'] == "Café Test" for cafe in cafes))

    # Resto de las pruebas sin cambios

if __name__ == '__main__':
    unittest.main()
