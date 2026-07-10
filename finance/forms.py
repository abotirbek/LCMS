from django import forms
from .models import Invoice, PaymentInvoice, Payment


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'issue_date',
            'due_date',
            'total_amount',
            'status',
            'enrollment',
        ]


class PaymentInvoiceForm(forms.ModelForm):
    class Meta:
        model = PaymentInvoice
        fields = [
            'invoice',
            'amount',
            'payment_date',
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = [
            'enrollment',
            'amount',
            'payment_date',
            'method',
        ]