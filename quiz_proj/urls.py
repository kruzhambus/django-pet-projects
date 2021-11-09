"""quiz_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index_main, index_metodichki, index_students_books, index_industrial, index_distance, index_practical
from django.conf.urls import url
from contact_form import views as contact_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('quiz/', include('quizes.urls', namespace = 'quizes')),
    path('', index_main, name = 'index_main'),
    path('method/',index_metodichki),
    path('students/books/', index_students_books),
    path('industrial/', index_industrial),
    path('distance/', index_distance),
    path('practical/', index_practical),
    path('hometasks/', include('homework.urls')),  # новое изменение
    url(r"^", include("users.urls")),           # accounts
    path('', include('contact_form.urls')),  # новое изменение
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)