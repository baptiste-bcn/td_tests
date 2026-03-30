from exceptions import CartePizzeriaException


class Pizza:
    def __init__(self, name: str, ingredients: list, price: float):
        self.name = name
        self.ingredients = ingredients
        self.price = price


class CartePizzeria:
    def __init__(self):
        self.pizzas = []

    def is_empty(self) -> bool:
        """Retourne True si la carte ne contient aucune pizza."""
        return len(self.pizzas) == 0

    def nb_pizzas(self) -> int:
        """Retourne le nombre total de pizzas sur la carte."""
        return len(self.pizzas)

    def add_pizza(self, pizza: Pizza):
        """Ajoute une instance de Pizza à la liste."""
        self.pizzas.append(pizza)

    def remove_pizza(self, name: str):
        """
        Retire la pizza par son nom.
        Lève CartePizzeriaException si le nom n'existe pas.
        """
        pizza_to_remove = None
        for p in self.pizzas:
            if p.name == name:
                pizza_to_remove = p
                break

        if pizza_to_remove:
            self.pizzas.remove(pizza_to_remove)
        else:
            raise CartePizzeriaException(f"La pizza '{name}' n'est pas dans la carte.")