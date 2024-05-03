from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context: dict = {
        "title": "Baby Land - Главная",
        "content": "Магазин детских игрушек BABY LAND",
    }

    return render(request, "catalog/index.html", context)


def about(request):
    context: dict = {
        "title": "Baby Land - О нас",
        "content": "О нас",
        "text_on_page": "Текст о том почему этот магазин такой классный, и какой хороший товар.",
    }

    return render(request, "catalog/about.html", context)


def dostavka(request):
    context: dict = {
        "title": "Baby Land - Доставка и оплата",
        "content": "Доставка и оплата",
        "text_on_page": "Вы можете забрать ваш заказ бесплатно в удобное для вас время в нашем магазине (с 09.00 до 20.00 пн-вс) ",
    }

    return render(request, "catalog/dostavka.html", context)


def inform(request):
    context: dict = {
        "title": "Baby Land - Контактная информация",
        "content": "Контактная информация",
        "text_on_page": "Адрес магазина: г.Гродно, телефон: (029)200-01-07",
    }

    return render(request, "catalog/inform.html", context)
