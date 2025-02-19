from django.db.models.fields import return_None
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')