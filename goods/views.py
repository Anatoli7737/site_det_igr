from django.shortcuts import render


def cataloge(request):
    return render(request, "goods/cataloge.html")


def product(request):
    return render(request, "goods/product.html")
