from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
# def novo_produto(request):
#     if request.method == "POST":