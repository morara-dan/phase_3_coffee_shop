class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = name

    def orders(self):
        customer_orders = []
        for order in Order._all_orders:
            if order.customer == self:
                customer_orders.append(order)
        return customer_orders

class Coffee:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) < 3:
            raise ValueError("Name must be at least 3 characters long")
        self._name = name

    @property
    def name(self):
        return self._name
    
class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        self._customer = customer

        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        self._coffee = coffee

        if not isinstance(price, float):
            raise TypeError("Price must be a float")
        if not (1.0 <= price <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = price
        
        Order._all_orders.append(self)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee