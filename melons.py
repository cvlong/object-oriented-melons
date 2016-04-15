"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Generalized Information for International & Domestic Melon Orders"""
    
    def __init__(self, species, qty, country_code = "U.S."):
        """Initialize melon order attributes"""

        print cheesecake
        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False

    def get_total(self):
        """Calculate price."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
