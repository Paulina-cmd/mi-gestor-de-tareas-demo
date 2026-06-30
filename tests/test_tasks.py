import unittest
from tasks import agregar_tarea, tareas

class TestTareas(unittest.TestCase):
    def test_agregar(self):
        agregar_tarea("Estudiar TBD")
        self.assertIn("Estudiar TBD", tareas)

if __name__ == '__main__':
    unittest.main()