# Voilation of OCP and we can remove jumky if and else using strategy patterns
import enum
class Payement(enum.Enum):
    CREDIT_CARD = 1
    DEBIT_CARD = 2
    GPAY = 3

class PaymentProcessor:
    def process_payment(self,payment_type:Payement):
        if payment_type == Payement.CREDIT_CARD:
            print("Credit Type Payment")
        elif payment_type == Payement.DEBIT_CARD:
            print("Dedit Type Payment")
        elif payment_type == Payement.GPAY:
            print("Gpay Type Payment")
        else:
            raise TypeError("Un supported Type")

if __name__ == "__main__":
    pp = PaymentProcessor()
    pp.process_payment(Payement.DEBIT_CARD)