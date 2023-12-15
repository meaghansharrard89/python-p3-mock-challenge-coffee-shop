class Coffee:
    def __init__(self, name):
        self.name = name

    # Coffee - name getter/setter
    @property
    def name(self):
        return self._name

    # Names must be of type str. Names length must be greater or equal to 3 characters. Should *not* be able to change after the coffee is instantiated:
    @name.setter
    def name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and len(name) >= 3:
            self._name = name

    # Returns a list of all orders for that coffee. Orders must be of type Order:
    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    # Returns a *unique* list of all customers who have ordered a particular coffee. Customers must be of type Customer:
    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    # Returns the total number of times a coffee has been ordered. Returns 0 if the coffee has never been ordered:
    def num_orders(self):
        increment = 1
        if any(order.coffee == self for order in Order.all):
            return sum(increment for order in Order.all if order.coffee == self)
        else:
            return 0

    # Returns the average price for a coffee based on its orders. Returns 0 if the coffee has never been ordered:
    def average_price(self):
        total = [order.price for order in Order.all if order.coffee == self]
        if not total:
            return 0
        else:
            return sum(total) / len(total)


class Customer:
    def __init__(self, name):
        self.name = name

    # Customer - name getter/setter
    @property
    def name(self):
        return self._name

    # Names must be of type str. Names must be between 1 and 15 characters, inclusive. Should be able to change after the customer is instantiated:
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name

    # Returns a list of all orders for that customer. Orders must be of type Order:
    def orders(self):
        return [order for order in Order.all if order.customer == self]

    # Returns a *unique* list of all coffees a customer has ordered. Coffees must be of type Coffee:
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    # Receives a coffee object and a price number as arguments. Creates and returns a new Order instance and associates it with that customer and the coffee object provided:
    def create_order(self, coffee, price):
        new_order = Order(customer=self, coffee=coffee, price=price)
        return new_order


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    # Coffee - price getter/setter
    @property
    def price(self):
        return self._price

    # Prices must be of type float. Price must be a number between 1.0 and 10.0, inclusive. Should not be able to change after the order is instantiated:
    @price.setter
    def price(self, price):
        if (
            isinstance(price, float)
            and 1.0 <= price <= 10.0
            and not hasattr(self, "price")
        ):
            self._price = price

    # Order - customer getter/setter
    @property
    def customer(self):
        return self._customer

    # Must be of type Customer:
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    # Order - coffee getter/setter
    @property
    def coffee(self):
        return self._coffee

    # Must be of type Coffee:
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
