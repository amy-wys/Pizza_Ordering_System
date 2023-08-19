class Payment:
    def creditcard(self):
        self.card_no = ""
        self.expiry_date = ""
        self.cardholder = ""
        self.cvv = ""

    def get_card(self):
        self.card_no = input("Enter your card number: ")
        self.expiry_date = input("Enter the card's expiry date: ")
        self.cardholder = input("Enter the cardholder name: ")
        self.cvv = input("Enter the CVV code: ")

