# test_pizzeria.py
import unittest
from unittest.mock import MagicMock
from pizzeria import CartePizzeria, Pizza, Drink
from exceptions import CartePizzeriaException


class TestCartePizzeria(unittest.TestCase):
    def setUp(self):
        self.carte = CartePizzeria()

    def test_add_element_general(self):
        # On teste le nouveau add() universel
        mock_item = MagicMock(spec=Drink)
        mock_item.name = "Cola"
        self.carte.add(mock_item)
        self.assertEqual(self.carte.nb_drinks(), 1)

    def test_remove_ok(self):
        mock_pizza = MagicMock(spec=Pizza)
        mock_pizza.name = "Calzone"
        # On utilise add() et pas add_pizza()
        self.carte.add(mock_pizza)
        self.carte.remove("Calzone")
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_doublon_ingredients_pizza(self):
        # On crée deux pizzas différentes par le nom mais identiques par recette
        p1 = Pizza("Reine", 10.0, "Miam", ["tomate", "champis"], "tomate")
        p2 = Pizza("Regina", 12.0, "Miam aussi", ["champis", "tomate"], "tomate")

        self.carte.add(p1)
        with self.assertRaises(CartePizzeriaException):
            self.carte.add(p2)  # Doit lever l'exception car ingrédients identiques