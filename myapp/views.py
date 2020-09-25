from django.shortcuts import render
from .forms import UrlModelForm
from . import models
from django.shortcuts import render, redirect

# Create your views here.
# def customise_url(request):
#     submitted = False
#     if request.method == "POST":
#         form = UrlModelForm(request.POST)
#         if form.is_valid():
#             new_data = form.save(commit=False)
#             new_data.creator = request.user
#             new_data.save()
#             new_form = UrlModelForm()
#             submitted = True
#             return render(
#                 request,
#                 "myapp/base.html",
#                 {"data": new_data, "form": new_form, "submitted": submitted},
#             )
#     else:
#         submitted = False
#         form = UrlModelForm()
#     return render(request, "myapp/base.html", {"form": form, "submitted": submitted})


# def new_url(request, keyword):
#     m = models.UrlModel.objects.get(keyword=keyword)
#     return redirect(m.original_url)


# def give_link(request):
#     return render(request, "myapp/new_link.html")

