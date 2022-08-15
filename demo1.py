class Item:
  def __init__(self, price, n, name):
    self.price = price
    self.amount = n
    self.name = name
   
item1 = Item(200, 5, "Кеды")
item2 = Item(500, 2, "Шорты")
print(item1.price)
print(item2.name)
