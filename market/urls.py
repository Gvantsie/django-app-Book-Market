from django.urls import path
from django.views.generic import RedirectView

from . import views
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/books/')),
    path('books/', views.get_books, name='get_books'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]
