from django.test import TestCase, Client
from .models import Laboratorio


class LaboratorioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Ejemplo de test
        Laboratorio.objects.create(
            nombre='Laboratorio 1', ciudad='Ciudad 1', pais='País 1')

    def test_datos_laboratorio_coinciden(self):
        laboratorio = Laboratorio.objects.get(nombre='Laboratorio 1')
        self.assertEqual(laboratorio.nombre, 'Laboratorio 1')
        self.assertEqual(laboratorio.ciudad, 'Ciudad 1')
        self.assertEqual(laboratorio.pais, 'País 1')


class LaboratorioURLTest(TestCase):
    def test_laboratorio_url_responde_con_exito(self):
        client = Client()
        response = client.get('/laboratorio/')
        self.assertEqual(response.status_code, 200)
