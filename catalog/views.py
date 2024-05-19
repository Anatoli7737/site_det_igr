from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories


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
        "text_on_page": "Мы работаем и радуем вас уже более 5 лет. Все товары сертифицированы. Мы уважаем и ценим каждого нашего клиента. У нас есть приятные бонусы нашим постоянным клиентам!",
    }

    return render(request, "catalog/about.html", context)


def dostavka(request):
    context: dict = {
        "title": "Baby Land - Доставка и оплата",
        "content": "Доставка и оплата",
        "text_on_page": "Вы можете забрать ваш заказ бесплатно в удобное для вас время в нашем магазине (с 09.00 до 20.00 пн-вс). Осуществляется доставка по городу (стоимость доставки зависит от района)",
    }

    return render(request, "catalog/dostavka.html", context)


def inform(request):
    context: dict = {
        "title": "Baby Land - Контактная информация",
        "content": "Контактная информация",
        "text_on_page": "Адрес магазина: г.Гродно, ул.Суворова, 127А. Телефон: (029)200-01-07",
    }

    return render(request, "catalog/inform.html", context)
