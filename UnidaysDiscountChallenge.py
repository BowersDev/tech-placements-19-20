"""
 * Copyright (C) 2018 Bowers Development - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 *
 * Inspired by the MyUNiDAYS Tech Placement programming challenge, Nov2018.
"""


items = {
    'a':{
        'price':8 # the base price of the item
    },
    'b':{
        'price':12,
        'discount':{ # define a discount
            'quantity':2, # the quantity needed to qualify for discount
            'price':20 # the new price of said quantity
        }
    },
    'c':{
        'price':4,
        'discount':{
            'quantity':3,
            'price':10
        }
    },
    'd':{
        'price':7,
        'discount':{
            'quantity':2,
            'price':7
        }
    },
    'e':{
        'price':5,
        'discount':{
            'quantity':3,
            'price':10
        }
    }
}


class UnidaysDiscountChallenge:
    def __init__(self):
        self.basket = {}

    def AddToBasket(self, item):
        if item in self.basket:
            self.basket[item] += 1
        else:
            self.basket[item] = 1

    def CalculateTotalPrice(self):
        price = 0

        for item in self.basket:
            quantity = self.basket[item]
            itemData = items[item]
            if 'discount' in itemData: # if item has discounts available
                noDiscountQuantity = (quantity % itemData['discount']['quantity']) # number of items for which a discount is not available
                price += ( itemData['price'] * noDiscountQuantity ) # added price for items not discounted

                discountSize = (quantity - noDiscountQuantity) / itemData['discount']['quantity'] # number of times the discount price is applied
                price += ( discountSize * itemData['discount']['price'] ) # added price with discount
            else:
                price += ( itemData['price'] * quantity ) # no discounts, so just add normal price * quantity

        priceResponse = {
            'total': price, # return total price
            'deliveryCharge': 7 if price > 0 and price <= 50 else 0 # delivery is £7 for atleast 1 item, total price less than £50. free for £50+
        }
        return priceResponse



example = UnidaysDiscountChallenge()
example.AddToBasket('e')
example.AddToBasket('d')
example.AddToBasket('c')
example.AddToBasket('b')
example.AddToBasket('a')

result = example.CalculateTotalPrice()

totalPrice = result['total']
deliveryCharge = result['deliveryCharge']
overallTotal = totalPrice + deliveryCharge

print(overallTotal)
