"""Classes for melon orders."""
class AbstractMelonOrder():

    shipped = False

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        
        self.species = species
        self.qty = qty
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        if species == christmas_melons:
            base_price = 1.5 * base_price

        if order_type == 'international' and qty < 10:
            flat_fee = 3
            base_price = base_price + flat_fee

        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = "domestic"

    
class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    order_type = "international"


class GovernmentMelonOrder(DomesticMelonOrder):
    """A US government melon order"""
    
    tax = 0.00
    passes_inspection = False

    def mark_inspection(passed):
        """Record the fact that an order has been inspected"""

        self.passes_inspection = passed
