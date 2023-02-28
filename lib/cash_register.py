#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.last_transaction = 0
    self.items = []

  def add_item(self, title, price, quantity = 1):
    self.last_transaction = price * quantity
    self.total += self.last_transaction
    # _ is a placeholder 
    for _ in range(quantity):
      self.items.append(title)
  
  #expecting an integer 
  def apply_discount(self):
    if (self.discount > 0):
      discount_percent = (100 - float(self.discount)) / 100 
      self.total = int(self.total * discount_percent)
      print(f"After the discount, the total comes to ${self.total}.")
    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
    self.total -= self.last_transaction





#void_last_transaction() method will remove the last transaction from the total.
# You'll need to make an additional attribute and keep track of that last transaction amount 
