from django.shortcuts import render
from .models import chaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm


def Home(request):
    chais = chaiVariety.objects.all()
    return render(request, "all_chai.html", {"chais": chais})


def chai_details(request, chai_id):
    chai = get_object_or_404(chaiVariety, pk=chai_id)
    return render(request, "chai_details.html", {"chai": chai})


def chai_stores_view(request):
    stores = None
    form = None
    if request.method == "POST":
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data["chai_Variety"]
            stores = Store.objects.filter(chai_variety=chai_variety)
    else:
        form = ChaiVarietyForm()
    return render(request, "chai_stores.html", {"stores": stores, "form": form})
