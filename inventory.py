class Inventory:
    """Manages the collection of products.

    Single Responsibility: store products, add products, search products,
    and display products. It does NOT represent a single product, load/save
    JSON files, or run the menu.
    """

    def __init__(self):
        self.__products = []

    def __find(self, product_id):
        """Private helper: return the Product with a matching ID, or None."""
        for product in self.__products:
            if product.get_id().lower() == product_id.strip().lower():
                return product
        return None

    def add_product(self, product):
        """Store a Product in the collection.

        Returns False if a product with the same ID already exists.
        """
        if self.__find(product.get_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):
        """Return the matching Product object, or None if not found."""
        return self.__find(product_id)

    def display_all(self):
        if not self.__products:
            print("No products in inventory.")
            return
        for product in self.__products:
            product.display_information()

    def get_products(self):
        """Return a copy of the product list (used when saving to JSON)."""
        return list(self.__products)