from abc import ABC, abstractmethod


# Define an abstract base class for Customer
class Customer(ABC):
    @abstractmethod
    def get_discount(self, amount):
        pass


# RegularCustomer class implementing get_discount
class RegularCustomer(Customer):
    def get_discount(self, amount):
        return amount * 0.1  # 10% discount


# VIPCustomer class implementing get_discount
class VIPCustomer(Customer):
    def get_discount(self, amount):
        return amount * 0.2  # 20% discount


# DiscountCalculator class using Customer interface
class DiscountCalculator:
    def calculate_discount(self, customer, amount):
        return customer.get_discount(amount)


# Usage example

calculator = DiscountCalculator()

print("\n\n")

discount = calculator.calculate_discount(RegularCustomer(), 100)
print(f"Discount for RegularCustomer on amount 100: {discount}")

discount = calculator.calculate_discount(VIPCustomer(), 100)
print(f"Discount for VIPCustomer on amount 100: {discount}")

print("\n\n")
