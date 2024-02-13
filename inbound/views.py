
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .forms import InboundForm
from .models import Inbound
from django.db.models import Q
from django.views.decorators.http import require_POST


from django.shortcuts import get_object_or_404

def inbound_detail(request, pk):
    item = get_object_or_404(Inbound, pk=pk)
    return render(request, 'inbound/inbound_detail.html', {'item': item})

def inbound_list(request):
    inbound_records = Inbound.objects.all()
    print(inbound_records)
    return render(request, 'inbound/inbound_list.html', {'inbound_records': inbound_records})


def add_inbound_item(request):
    if request.method == 'POST':
        form = InboundForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inbound_list')
    else:
        form = InboundForm()
    return render(request, 'inbound/add_inbound_item.html', {'form': form})


#for searching
def inbound_list(request):
    search_query = request.GET.get('search', '')  
    if search_query:
        inbound_records = Inbound.objects.filter(
            Q(reference__icontains=search_query) |
            Q(product_sku__icontains=search_query) |
            Q(location__icontains=search_query)
        )
    else:
        inbound_records = Inbound.objects.all()
    return render(request, 'inbound/inbound_list.html', {'inbound_records': inbound_records})

def update_inbound(request, pk):
    inbound = get_object_or_404(Inbound, pk=pk)
    if request.method == 'POST':
        form = InboundForm(request.POST, instance=inbound)
        if form.is_valid():
            form.save()
            return redirect('inbound_list')  
    else:
        form = InboundForm(instance=inbound)
    return render(request, 'inbound/edit_inbound.html', {'form': form})


@require_POST 
def delete_inbound(request, pk):
    inbound = get_object_or_404(Inbound, pk=Inbound.objects.id)
    inbound.delete()
    return redirect('inbound_list')
