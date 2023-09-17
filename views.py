from django.shortcuts import render


def home(request):
    return render(request, 'myapp/home.html')


def admin_page(request):
    return render(request, 'myapp/admin.html')


def styled_page(request):
    return render(request, 'myapp/styled.html')


