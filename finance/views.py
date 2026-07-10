from django.shortcuts import render, redirect, get_object_or_404
from .forms import InvoiceForm, PaymentInvoiceForm, PaymentForm
from .models import Invoice, PaymentInvoice, Payment


# INVOICE --- CRUD
def get_invoice(request):
    invoices = Invoice.objects.all()
    return render(request, 'finance/invoice/invoice_list.html', {'invoices': invoices})


def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'finance/invoice/create_invoice.html', {'form': form})


def read_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    return render(request, 'finance/invoice/read_invoice.html', {'invoice': invoice})


def update_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'finance/invoice/create_invoice.html', {'form': form})


def delete_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        invoice.delete()
        return redirect('invoice_list')
    return render(request, 'finance/invoice/delete_invoice.html', {'invoice': invoice})


# PAYMENT INVOICE --- CRUD
def get_payment_invoice(request):
    payment_invoices = PaymentInvoice.objects.all()
    return render(request, 'finance/payment_invoice/payment_invoice_list.html', {'payment_invoices': payment_invoices})


def create_payment_invoice(request):
    if request.method == 'POST':
        form = PaymentInvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_invoice_list')
    else:
        form = PaymentInvoiceForm()
    return render(request, 'finance/payment_invoice/create_payment_invoice.html', {'form': form})


def read_payment_invoice(request, pk):
    payment_invoice = get_object_or_404(PaymentInvoice, pk=pk)
    return render(request, 'finance/payment_invoice/read_payment_invoice.html', {'payment_invoice': payment_invoice})


def update_payment_invoice(request, pk):
    payment_invoice = get_object_or_404(PaymentInvoice, pk=pk)
    if request.method == 'POST':
        form = PaymentInvoiceForm(request.POST, instance=payment_invoice)
        if form.is_valid():
            form.save()
            return redirect('payment_invoice_list')
    else:
        form = PaymentInvoiceForm(instance=payment_invoice)
    return render(request, 'finance/payment_invoice/create_payment_invoice.html', {'form': form})


def delete_payment_invoice(request, pk):
    payment_invoice = get_object_or_404(PaymentInvoice, pk=pk)
    if request.method == 'POST':
        payment_invoice.delete()
        return redirect('payment_invoice_list')
    return render(request, 'finance/payment_invoice/delete_payment_invoice.html', {'payment_invoice': payment_invoice})


# PAYMENT --- CRUD
def get_payment(request):
    payments = Payment.objects.all()
    return render(request, 'finance/payment/payment_list.html', {'payments': payments})


def create_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'finance/payment/create_payment.html', {'form': form})


def read_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    return render(request, 'finance/payment/read_payment.html', {'payment': payment})


def update_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'finance/payment/create_payment.html', {'form': form})


def delete_payment(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    if request.method == 'POST':
        payment.delete()
        return redirect('payment_list')
    return render(request, 'finance/payment/delete_payment.html', {'payment': payment})
