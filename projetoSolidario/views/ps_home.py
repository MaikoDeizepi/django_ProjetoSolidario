from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="projetosolidario:index")
def home(request):

    return render(
        request,
        "projetoSolidario/home.html",
    )
