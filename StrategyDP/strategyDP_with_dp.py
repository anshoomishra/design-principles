# Voilation of OCP and we can remove jumky if and else using strategy patterns
from abc import ABC,abstractmethod
import enum
class Payement(enum.Enum):
    CREDIT_CARD = 1
    DEBIT_CARD = 2
    GPAY = 3
class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self,payment_type:Payement):
        pass

class DebitCardPaymentProcessor(PaymentStrategy):
    def process_payment(self,payment_type:Payement):
        print("Debit card processing payment.......")

class CreditCardPaymentProcessor(PaymentStrategy):
    def process_payment(self,payment_type:Payement):
        print("Credit card processing payment.......")

if __name__ == "__main__":
    dcp = DebitCardPaymentProcessor()
    dcp.process_payment(Payement.DEBIT_CARD)