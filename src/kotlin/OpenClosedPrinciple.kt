@file:Suppress("unused")

package kotlin

// Define an interface for Customer
interface Customer {
    fun getDiscount(amount: Double): Double
}

// RegularCustomer class implementing Customer interface
class RegularCustomer : Customer {
    override fun getDiscount(amount: Double): Double {
        return amount * 0.1 // 10% discount
    }
}

// VIPCustomer class implementing Customer interface
class VIPCustomer : Customer {
    override fun getDiscount(amount: Double): Double {
        return amount * 0.2 // 20% discount
    }
}

// DiscountCalculator class using Customer interface
class DiscountCalculator {
    fun calculateDiscount(customer: Customer, amount: Double): Double {
        return customer.getDiscount(amount)
    }
}