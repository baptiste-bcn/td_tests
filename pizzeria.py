from exceptions import CartePizzeriaException


class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class Pizza(MenuItem):
    def __init__(self, name, price, description, ingredients, base):
        super().__init__(name, price)
        self.description = description
        self.ingredients = list(ingredients)
        self.base = base  # "tomate" ou "crème"


class Drink(MenuItem):
    def __init__(self, name, price, is_alcoholic: bool):
        super().__init__(name, price)
        self.is_alcoholic = is_alcoholic


class Dessert(MenuItem):
    def __init__(self, name, price, ingredients, is_homemade: bool):
        super().__init__(name, price)
        self.ingredients = list(ingredients)
        self.is_homemade = is_homemade


class CartePizzeria:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def nb_pizzas(self):
        return len([e for e in self.elements if isinstance(e, Pizza)])

    def nb_drinks(self):
        return len([e for e in self.elements if isinstance(e, Drink)])

    def nb_desserts(self):
        return len([e for e in self.elements if isinstance(e, Dessert)])

    def add(self, element):
        # Règle 1 : Vérification du nom
        if any(e.name == element.name for e in self.elements):
            raise CartePizzeriaException(f"L'élément {element.name} existe déjà.")

        # Règle 2 : Doublons de Pizza (ingrédients + base)
        if isinstance(element, Pizza):
            for e in self.elements:
                if isinstance(e, Pizza):
                    if (
                        set(e.ingredients) == set(element.ingredients)
                        and e.base == element.base
                    ):
                        raise CartePizzeriaException("Une pizza identique existe déjà.")

        self.elements.append(element)

    def remove(self, name):
        for e in self.elements:
            if e.name == name:
                self.elements.remove(e)
                return
        raise CartePizzeriaException(f"L'élément {name} n'existe pas.")
