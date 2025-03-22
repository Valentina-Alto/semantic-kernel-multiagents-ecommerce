from semantic_kernel.functions import kernel_function
import requests

class CartPlugin:
    """
    Plugin to handle cart operations.
    """
    def __init__(self, base_url) -> None:
        self.base_url = base_url

    @kernel_function(name="add_to_cart",
                     description="Add an item to the cart.")
    def add_to_cart(self, item_name: str, item_price: float) -> str:
        """Add an item to the cart."""
        url = f'{self.base_url}/cart'  # Ensure this matches the JSON Server endpoint
        cart_item = {
            'name': item_name,
            'price': item_price
        }

        response = requests.post(url, json=cart_item)

        if response.status_code == 201:
            return f"Item '{item_name}' added to cart successfully."
        else:
            return f"Failed to add item to cart: {response.status_code} {response.text}"

