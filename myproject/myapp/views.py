from django.shortcuts import render

#user details
from django.shortcuts import redirect
from .forms import UserDetailForm

# selling progress
from .models import UserDetail


# Create your views here.

def home(request):
    return render(request, "home.html")

def aboutus(request):
    return render(request, "aboutus.html")

def allitems(request):
    return render(request, "allitems.html")



def user_details_view(request):
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = UserDetailForm()
    return render(request, 'user_details_form.html', {'form': form})



def selling_progress_view(request):
    user_details = UserDetail.objects.all()
    return render(request, 'selling_progress.html', {'user_details': user_details})


# for the jewel items pages

from django.shortcuts import get_object_or_404
from .models import Item

def all_items(request):
    items = Item.objects.all()
    return render(request, 'allitems.html', {'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'item_detail.html', {'item': item})


# searchbar and gender dropdown functionality
from django.db.models import Q

def search_items(request):
    query = request.GET.get('q')
    gender = request.GET.get('gender')

    items = Item.objects.all()

    if query:
        items = items.filter(
            Q(type__icontains=query) |
            Q(material__icontains=query) |
            Q(style__icontains=query) |
            Q(occasion__icontains=query) |
            Q(other_details__icontains=query)
        )

    if gender:
        items = items.filter(gender=gender)

    return render(request, 'allitems.html', {'items': items})
