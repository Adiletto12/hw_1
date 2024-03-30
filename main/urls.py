
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from book.views import BookListView, BookDetailView, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookListView.as_view()),
    path('book/<int:id>/', BookDetailView.as_view()),
    path('', include('comment.urls')),
    path('', include('parser.urls')),
    path('', include('parser_m3.urls')),
    path('search/', SearchView.as_view(), name='search'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

