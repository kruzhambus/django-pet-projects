from django.shortcuts import render

from django.views.generic import ListView

from .models import Homework


# def homework(request):
#     homeworks = Homework.objects.all()
#     context = {
#         'title': Homework.title,
#         #'author'
#     }


class BlogListView(ListView):
    paginate_by = 3
    model = Homework
    template_name = 'home.html'
    ordering = ['-created_at']      # done


def add_news(request):
    return render(request, 'homework/hw_ad.html')

# Create your views here.
