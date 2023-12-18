class Coffee:
    def __init__(self, name):
        self.name = name

    # Coffee - name getter/setter:
    @property
    def name(self):
        return self._name

    # Names must be of type str. Names length must be greater or equal to 3 characters. Should *not* be able to change after the coffee is instantiated:
    @name.setter
    def name(self, name):
        if not hasattr(self, "name") and isinstance(name, str) and len(name) > 3:
            self._name = name
        else:
            raise Exception

    # Returns a list of all orders for that coffee. Orders must be of type Order:
    def orders(self):
        return [order for order in Order.all if order.coffee == self]

    # Returns a *unique* list of all customers who have ordered a particular coffee. Customers must be of type Customer:
    def customers(self):
        return list(set([order.customer for order in self.orders()]))

    # Returns the total number of times a coffee has been ordered. Returns 0 if the coffee has never been ordered:
    def num_orders(self):
        return len(self.orders())

    # Returns the average price for a coffee based on its orders. Returns 0 if the coffee has never been ordered:
    def average_price(self):
        total = [order.price for order in self.orders()]
        average = sum(total) / len(total)
        return average


class Customer:
    def __init__(self, name):
        self.name = name

    # Customer - name getter/setter:
    @property
    def name(self):
        return self._name

    # Names must be of type str. Names must be between 1 and 15 characters, inclusive. Should be able to change after the customer is instantiated:
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise Exception

    # Returns a list of all orders for that customer. Orders must be of type Order:
    def orders(self):
        return [order for order in Order.all if order.customer == self]

    # Returns a *unique* list of all coffees a customer has ordered. Coffees must be of type Coffee:
    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    # Receives a coffee object and a price number as arguments. Creates and returns a new Order instance and associates it with that customer and the coffee object provided:
    def create_order(self, coffee, price):
        return Order(customer=self, coffee=coffee, price=price)

    # Receives a coffee object argument. Returns the Customer instance that has spent the most money on the coffee instance provided as argument. Returns None if there are no customers for the coffee instance provided:
    @classmethod
    def most_aficionado(cls, coffee):
        all_customers = [order.customer for order in coffee.orders()]
        if not all_customers:
            return None
        most_spent_customer = max(
            all_customers,
            key=lambda customer: sum(
                order.price for order in customer.orders() if order.coffee == coffee
            ),
        )
        return most_spent_customer


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    # Order - price getter/setter:
    @property
    def price(self):
        return self._price

    # Prices must be of type float. Price must be a number between 1.0 and 10.0, inclusive. Should *not* be able to change after the order is instantiated:
    @price.setter
    def price(self, price):
        if (
            not hasattr(self, "price")
            and isinstance(price, (float, int))
            and 1.0 <= price <= 10.0
        ):
            self._price = float(price)
        else:
            raise Exception

    # Order - customer getter/setter:
    @property
    def customer(self):
        return self._customer

    # Must be of type Customer:
    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    # Order - coffee getter/setter:
    @property
    def coffee(self):
        return self._coffee

    # Must be of type Coffee:
    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
