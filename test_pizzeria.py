import unittest
from unittest.mock import MagicMock
from pizzeria import CartePizzeria, Pizza
from exceptions import CartePizzeriaException


class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        # On initialise une carte vide avant chaque test
        self.carte = CartePizzeria()

    def test_is_empty_au_demarrage(self):
        self.assertTrue(self.carte.is_empty())

    def test_nb_pizzas_initial(self):
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_add_pizza_mockee(self):
        # On crée un Mock qui se fait passer pour une Pizza
        mock_pizza = MagicMock(spec=Pizza)
        mock_pizza.name = "Marguerita"

        self.carte.add_pizza(mock_pizza)

        self.assertFalse(self.carte.is_empty())
        self.assertEqual(self.carte.nb_pizzas(), 1)

    def test_remove_pizza_ok(self):
        mock_pizza = MagicMock(spec=Pizza)
        mock_pizza.name = "Calzone"
        self.carte.add_pizza(mock_pizza)

        # On vérifie que la suppression fonctionne
        self.carte.remove_pizza("Calzone")
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_remove_pizza_inexistante_leve_exception(self):
        # On vérifie que l'erreur est bien levée
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("PizzaQuiNexistePas")


if __name__ == '__main__':
    unittest.main()