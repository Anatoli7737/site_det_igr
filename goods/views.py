from django.shortcuts import render


def cataloge(request):
    context = {
        "title": "Baby Land - Каталог",
        "goods": [
            {
                "image": "deps/images/goods/lego_garazh.jpg",
                "name": "Конструктор LEGO Гараж",
                "description": "Пройдите диагностику и ремонт в автосервисе из конструктора Lego City Custom Car Garage. Здесь есть всё для заботы о любимых машинках!",
                "price": 180.00,
            },
            {
                "image": "deps/images/goods/lego_minicraaft.jpg",
                "name": "Конструктор LEGO Минекрафт",
                "description": "Отправляйтесь в приключение с набором Lego Minecraft The Swamp Adventure! Помогите Алексу пройти через мангровые болота и отразить атаки зомби.",
                "price": 93.00,
            },
            {
                "image": "deps/images/goods/kukla_barbie3.jpg",
                "name": "Кукольный набор Barbie Пекарня",
                "description": "Кукольный набор Barbie Пекарня – почувствуй себя настоящим кондитером. Набор для девочек вместе с неповторимой куклой Барби воплотит в реальность мечту каждой девочки.",
                "price": 88.00,
            },
            {
                "image": "deps/images/goods/kukla_barbie44.jpg",
                "name": "Кукла Barbie Mattel Спальня",
                "description": "Набор для спальни Барби вдохновляет рассказывать удивительные истории вечером и утром.",
                "price": 107.00,
            },
            {
                "image": "deps/images/goods/moi_pitomec.jpg",
                "name": "Игрушка Мой питомец Щенок Молли",
                "description": "Интерактивная игрушка Мой питомец Щенок Молли станет добрым другом для вашего ребёнка.",
                "price": 230.00,
            },
            {
                "image": "deps/images/goods/moi_mishka.jpg",
                "name": "Мягкая игрушка Медведь Мика",
                "description": "Медведь Мика – самый обаятельный и верный друг. Этот плюшевый мишка маленький и нежный: его шубка не только теплая, но еще и очень мягкая.",
                "price": 120.00,
            },
            {
                "image": "deps/images/goods/pazzle_1.jpg",
                "name": "Пазлы для детей На ферме",
                "description": "Игра с пазлами поможет развить усидчивость, мелкую моторику рук, а также научит находить связь между частью и целым.",
                "price": 65.00,
            },
            {
                "image": "deps/images/goods/mozaika_5.jpg",
                "name": "Детская развивающая мозаика",
                "description": "Подарите вашему ребёнку увлекательную развивающую мозаику.",
                "price": 75.00,
            },
            {
                "image": "deps/images/goods/game_1.jpg",
                "name": "Настольная игра Азбука на картинках",
                "description": "Изучайте буквы в легкой игровой форме вместе с вашим малышом. А красочные картинки превратят обучение в веселую игру!",
                "price": 77.00,
            },
            {
                "image": "deps/images/goods/game_321.jpg",
                "name": "Пластик на липучках Времена года",
                "description": "Игра развивает координацию движений, интеллект и память, внимание и усидчивость, учит сопоставлять объекты между собой, расширяет словарный запас.",
                "price": 91.00,
            },
            {
                "image": "deps/images/goods/toys_1.jpg",
                "name": "Игрушка Развивающий комплекс",
                "description": "Отличная игра для знакомства с окружающим миром.",
                "price": 69.00,
            },
            {
                "image": "deps/images/goods/zaika_1.jpg",
                "name": "Игрушка Умный зайка",
                "description": "Умный зайка - незаменимый помощник для мамы и лучший друг для малыша. Познакомит малыша с миром звуков и цветов, будет рассказывать сказки и стишки, петь песенки и сладкие колыбельные",
                "price": 58.00,
            },
        ],
    }
    return render(request, "goods/cataloge.html", context)


def product(request):
    return render(request, "goods/product.html")
