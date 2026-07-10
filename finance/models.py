from django.db import models
from common.models import CommonAll
from students.models import Enrollment

# Create your models here.
class Invoice(CommonAll):
    issue_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="invoices")

    def __str__(self):
        return str(self.id)

class PaymentInvoice(CommonAll):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()

    def __str__(self):
        return str(self.id)

class Payment(CommonAll):
    PAYMENT_METHODS  = (
        ('cash', 'Cash'),
        ('card', 'Card'),
        ('bank', 'Bank'),
    )
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name="payments")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    method = models.CharField(max_length=4, choices=PAYMENT_METHODS)

    def __str__(self):
        return str(self.id)