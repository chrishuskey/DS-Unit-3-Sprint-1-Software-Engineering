"""
Module to generate random Acme Corp. products, and print a summary of them.
"""

from acme import Product
import random
import statistics


# Fixed lists:
PRODUCT_ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
RANDOM_NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products_list = []
    for product in range(num_products):
        name = str(
            f"{random.sample(PRODUCT_ADJECTIVES, 1)[0]} {random.sample(RANDOM_NOUNS, 1)[0]}")
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        new_product = Product(name, price, weight, flammability)
        products_list.append(new_product)
    return products_list


def inventory_report(list_of_products):
    print("ACME CORPORATION INVENTORY REPORT:")
    n_unique_products = len(set(list_of_products))
    print(f"Unique product names: {n_unique_products}")
    # Get average price, weight and flammability for the products in a list.
    prices = []
    weights = []
    flammabilities = []
    for product in list_of_products:
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)
    print(f"Average price: {statistics.mean(prices):.2f}")
    print(f"Average weight: {statistics.mean(weights):.2f}")
    print(f"Average flammability: {statistics.mean(flammabilities):.2f}")


if __name__ == '__main__':
    inventory_report(generate_products())
