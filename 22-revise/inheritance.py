# Base class payment

class Payment:

    def __init__(self,amount, currency):
        self.amount= amount
        self.currency = currency

    def make_payment(self):
        print(f"Payment of {self.amount} {self.currency} initiated.")

class UPIPayment(Payment):
    def __init__(self,amount,currency,uip_id):
        super().__init__(amount,currency)
        self.upi_id=uip_id

    def make_payment(self):
       # return super().make_payment()
        print(f"Payment of {self.amount} {self.currency} initiated using upi_id {self.upi_id}.")


class PayPalPayment(Payment):

    def __init__(self,amount,currency,paypal_email):
        super().__init__(amount,currency)
        self.paypal_email=paypal_email
    
    def make_payment(self):
       # return super().make_payment()
        print(f"Payment of {self.amount} {self.currency} initiated using paypal email {self.paypal_email}.")


class NetBanking(Payment):

    def __init__(self,amount,currency,bank_name,account_number):
        super().__init__(amount,currency)
        self.bank_name=bank_name
        self.account_number= account_number

    def make_payment(self):
       # return super().make_payment()
        print(f"Payment of {self.amount} {self.currency} initiated using bank {self.bank_name} from account  {self.account_number}.")




# p= Payment(100.123,"rupees")
# p.make_payment()

p=UPIPayment(12213.123,"Rupees","JitenP@OkAxis")
p.make_payment()


# Payment
#     amount
#     currency
#     make_payment()

# UPIPayment --> Payment
#     upi_id
#     make_payment()


# PayPalPayment --> Payment
#     paypal_email
#     make_payment()

# NetBanking --> Payment
#   bank_name
#   account_number
#   make_payment()