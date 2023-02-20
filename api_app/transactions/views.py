from django.shortcuts import render
from rest_framework.views import APIView
from .models import Transaction
from django.db.models import Max
import io, csv
from django.http import HttpResponse


class TransactionView(APIView):
    
    def post(self, request):
        url = request.body.decode('utf-8') 
        csvfiles = csv.DictReader(io.StringIO(url))
        for row in csvfiles:
            transaction = Transaction(
                        reference=row['reference'],
                        timestamp=row['timestamp'],
                        amount=row['amount'],
                        currency=row['currency'],
                        description=row['description'])
            transaction.save()
        return HttpResponse()


    def get(self, request):
        transactions = Transaction.objects.all().order_by('-timestamp')
        max_amount = Transaction.objects.aggregate(Max('amount'))['amount__max']
        return render(request, 'transactions/all_transactions.html',
                     {'transactions': transactions,'max_amount':max_amount})


def home(request):
    return render(request, 'transactions/home.html')
        

