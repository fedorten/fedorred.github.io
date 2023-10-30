from django.shortcuts import render


def index(request):
    data = {
        'title': 'главная страница!',
        'values': ['some', 'hello', '123'],
        'obj': {
            'car': 'lada',
            'age': 16,
            'habby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


