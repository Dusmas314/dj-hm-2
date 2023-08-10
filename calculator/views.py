from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def recipe_handler(request, dish):
    result = int(request.GET.get('servings', 1))
    recipe = DATA[dish].copy()
    recipe.update((key, round(value * result, 2)) for key, value in recipe.items())
    return render(request, 'calculator/index.html', {'recipe': recipe})


def omlet(request):
    return recipe_handler(request, 'omlet')


def pasta(request):
    return recipe_handler(request, 'pasta')


def buter(request):
    return recipe_handler(request, 'buter')




