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

    def coffees(self):
        ordered_coffees = []
        for order in Order._all_orders:
            if order.customer == self:
                if order.coffee not in ordered_coffees:
                    ordered_coffees.append(order.coffee)
        return ordered_coffees

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

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

    def orders(self):
        coffee_orders = []
        for order in Order._all_orders:
            if order.coffee == self:
                coffee_orders.append(order)
        return coffee_orders

    def customers(self):
        coffee_customers = []
        for order in Order._all_orders:
            if order.coffee == self:
                if order.customer not in coffee_customers:
                    coffee_customers.append(order.customer)
        return coffee_customers

    def num_orders(self):
        count = 0
        for order in Order._all_orders:
            if order.coffee == self:
                count += 1
        return count

    def average_price(self):
        total_price = 0.0
        order_count = 0
        for order in Order._all_orders:
            if order.coffee == self:
                total_price += order.price
                order_count += 1
        
        if order_count == 0:
            return 0.0
        return total_price / order_count
    
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
    



coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

customer1 = Customer("Dan")
customer2 = Customer("Imani")

print(f"Created coffee: {coffee1.name}")
print(f"Created coffee: {coffee2.name}")

print(f"Created customer: {customer1.name}")
print(f"Created customer: {customer2.name}")