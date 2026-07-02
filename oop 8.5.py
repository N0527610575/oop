from builtins import property, staticmethod, print


class Product:

    TAX_RATES = {
        'food': 0.0,
        'books': 0.0,
        'electronics': 0.17,
        'clothing': 0.17,
        'other': 0.17
    }


    def __init__(self, name, base_price, category='other', discount_percent=0):
        self._name = name


        self._base_price = 0
        self._category = 'other'
        self._discount_percent = 0


        self.base_price = base_price
        self.category = category
        self.discount_percent = discount_percent


    @property
    def name(self):
        return self._name


    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        if value < 0:
            print("שגיאה: מחיר לא יכול להיות שלילי")
        else:
            self._base_price = value


    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if value in Product.TAX_RATES:
            self._category = value
        else:
            print("שגיאה: קטגוריה לא חוקית")


    @property
    def discount_percent(self):
        return self._discount_percent

    @discount_percent.setter
    def discount_percent(self, value):
        if 0 <= value <= 100:
            self._discount_percent = value
        else:
            print("חייב להיות בין 0 ל-100")

    @property
    def price_after_discount(self):
        return self._base_price * (1 - self._discount_percent / 100)


    @property
    def tax_amount(self):

        rate = Product.get_tax_rate(self._category)
        return self.price_after_discount * rate


    @property
    def final_price(self):
        return self.price_after_discount + self.tax_amount


    @staticmethod
    def get_tax_rate(category):
        return Product.TAX_RATES.get(category, Product.TAX_RATES['other'])

    @staticmethod
    def calculate_bulk_discount(quantity, unit_price):
        if quantity >= 100:
            discount_rate = 0.15
        elif 50 <= quantity <= 99:
            discount_rate = 0.10
        elif 10 <= quantity <= 49:
            discount_rate = 0.05
        else:
            discount_rate = 0.0

        total_before_discount = quantity * unit_price
        return total_before_discount * discount_rate