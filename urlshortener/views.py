from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from myapp.forms import UrlModelForm
from myapp.models import UrlModel
import uuid

# Create your views here.
def home(request):
    data = []
    if request.user.is_authenticated:
        data = UrlModel.objects.all().filter(creator=request.user)
    if request.method == "POST":
        form = UrlModelForm(request.POST)  # form is object of urlmodelform
        if form.is_valid():
            new_data = form.save(commit=False)  # new_data is object of urlModel,
            # (commit = false mtlb abhi db me save ni hua h)
            val = uuid.uuid1()
            if len(new_data.keyword) == 0:
                new_data.keyword = val
            new_data.creator = request.user
            new_data.save()
            return redirect("home")
    else:
        form = UrlModelForm()
    return render(request, "myapp/base.html", {"form": form, "data": data})


def new_url(request, keyword):
    m = UrlModel.objects.get(keyword=keyword)
    return redirect(m.original_url)

