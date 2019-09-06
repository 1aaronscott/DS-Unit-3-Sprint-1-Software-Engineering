#!/usr/bin/env python3

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    # TODO - your code! Generate and add random products.
    for _ in range(num_products):
        # create name, price, weight, flammability for each
        name = sample(ADJECTIVES, 1)[0] + " " + sample(NOUNS, 1)[0]
        price = randint(5, 101)
        weight = randint(5, 101)
        flammability = uniform(0.0, 2.5)
        prod = Product(name, price, weight, flammability)
        products.append(prod)
        #print(name, price, weight, flammability)
        # print(prod.__dict__)
        # print(products)
    return products


def inventory_report(products):
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    total_price = 0
    total_weight = 0
    total_flammability = 0
    unique_list = []
    num_list = len(products)
    for prod in products:
        total_price += prod.price
        total_weight += prod.weight
        total_flammability += prod.flammability
        if prod.name not in unique_list:
            unique_list.append(prod.name)
    print("Unique product names: ", len(unique_list))
    print("Average price: ", total_price/num_list)
    print("Average weight: ", total_weight/num_list)
    print("Average flammability: ", total_flammability/num_list)


if __name__ == '__main__':
    inventory_report(generate_products())
