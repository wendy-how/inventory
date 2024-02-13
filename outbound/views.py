from django.shortcuts import render,redirect
from .models import Outbound
from .forms import OutboundForm
from django.db.models import Q

def outbound_list(request):
    outbound_records = Outbound.objects.all()
    return render(request, 'outbound/outbound_list.html', {'outbound_records': outbound_records})

def add_outbound_item(request):
    if request.method == 'POST':
        form = OutboundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('outbound_list')
    else:
        form = OutboundForm()
    return render(request, 'outbound/add_outbound_item.html', {'form': form})



def outbound_list(request):
    search_query = request.GET.get('search', '') 
    if search_query:
        outbound_records = Outbound.objects.filter(
            Q(reference__icontains=search_query) |
            Q(product_sku__icontains=search_query) |
            Q(destination__icontains=search_query)
        )
    else:
        outbound_records = Outbound.objects.all()
    return render(request, 'outbound/outbound_list.html', {'outbound_records': outbound_records})