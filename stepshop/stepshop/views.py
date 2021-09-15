from django.shortcuts import render


def index(request):

    title = 'главная'

    context = {
        'title': title,
    }

    return render(request, 'stepshop/index.html', context)


def contacts(request):

    title = 'контакты'

    context = {
        'title': title,
    }

    return render(request, 'stepshop/contact.html', context)


def about(request):

    title = 'о нас'

    context = {
        'title': title,
    }
    return render(request, 'stepshop/about.html', context)
