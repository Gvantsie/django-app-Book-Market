from django.forms import model_to_dict
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from market.models import Book


# Create your views here.
def get_books(request):
    books = Book.objects.all().filter(stock__gt=0).order_by('title')
    # book_data = list(books.values())
    # return JsonResponse({
    #     'books': book_data
    # })
    return render(request, 'index.html', {'books': books})


def book_detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        book_data = model_to_dict(book)
        return JsonResponse({'book': book_data})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)