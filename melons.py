class AbstractMelonOrder(object):
    """Generalized Information for International & Domestic Melon Orders"""
    
    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False


    # def get_total(self):
    #     """Calculate price."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price
    #     return total


    def get_total_holiday(self):
        """Calculate total price, higher price for international and Xmas melons"""

        base_price = 5

        if self.species == "Christmas melon":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        
        if self.order_type == "international":
            if self.qty < 10:
                total = total + 3
        
        return total


    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    def __init__(self, species, qty):
        """Initialize a domestic melon order"""
        super(DomesticMelonOrder, self).__init__(species, qty)
        
        self.order_type = "domestic"
        self.tax = 0.08


    # order_type = "domestic"
    # tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize an international melon order"""
        super(InternationalMelonOrder, self).__init__(species, qty)
        
        self.order_type = "international"
        self.tax = 0.17
        self.country_code = country_code


    # order_type = "international"
    # tax = 0.17

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code
