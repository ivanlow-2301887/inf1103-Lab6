class Product:
    """Represents a single product in the inventory.

    Single Responsibility: store product information and manage its own
    state. This class does NOT load/save JSON files, display the menu,
    or ask the user for input.
    """

    def __init__(self, product_id, name, price, stock):
        # __ prefix = intended private (encapsulation). External code must
        # go through the public methods below instead of editing these.
        self.__product_id = str(product_id)
        self.__name = name
        self.__price = float(price)
        self.__stock = int(stock)

    # ---------- public interface (getters) ----------

    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # ---------- behaviour ----------

    def update_stock(self, quantity):
        """Set the stock to a new quantity.

        The Product decides how the value is treated before assigning it
        internally (encapsulation). Returns True on success.
        """
        try:
            quantity = int(quantity)
        except (TypeError, ValueError):
            return False
        if quantity < 0:
            return False
        self.__stock = quantity
        return True

    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")

    # ---------- JSON support ----------

    def to_dict(self):
        """Convert to a plain dictionary so it can be saved as JSON."""
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Product from a dictionary loaded from JSON."""
        return cls(data["id"], data["name"], data["price"], data["stock"])