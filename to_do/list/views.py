from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from .models import to_do
from .forms import todoform

def index(request):
     item_list = to_do.objects.order_by("-date")
     if request.method=="POST":
          form=todoform(request.POST)
          if form.is_valid():
               form.save()
               return redirect('to_do')
     form = todoform()
     page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
     return render(request, 'to_do/index.html', page)

def remove(request, item_id):
    item = to_do.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('to_do')