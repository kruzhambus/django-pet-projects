from django.shortcuts import render

def index_main(request):
    return render(request, 'main.html')

def index_metodichki(request):
    return render(request, 'metodichki.html')

def index_students_books(request):
    return render(request, 'books.html')

def index_industrial(request):
    return render(request, 'industrial.html')

def index_distance(request):
    return render(request, 'distance.html')

def index_practical(request):
    return render(request, 'practical.html')
