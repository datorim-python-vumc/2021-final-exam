from django.shortcuts import (
    render,
    redirect,
)

from django.views.generic import (
    View,
    ListView,
    DetailView,
)

from django.urls import reverse_lazy

import deposits.models as models
from deposits.deposit import Deposit


class DepositListView(ListView):
    model = models.Deposit
    template_name = 'deposit_list.html'


class DepositDetailView(DetailView):
    model = models.Deposit
    template_name = 'deposit_detail.html'


class CreateDepositView(View):

    def get(self, request):

        return render(
            template_name='create_deposit.html',
            request=request,
        )

    def post(self, request):
        
        term_deposit = Deposit(
            deposit=int(request.POST['deposit']),
            term=int(request.POST['term']),
            rate=float(request.POST['rate']),
        )

        deposit = models.Deposit(
            deposit=term_deposit.deposit,
            term=term_deposit.term,
            rate=term_deposit.rate,
            interest=term_deposit.interest(),
        )

        deposit.save()

        return redirect(reverse_lazy('deposit-list'))


