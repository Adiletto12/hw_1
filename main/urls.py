
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from book.views import books_view, books_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books_view),
    path('book/<int:id>/', books_detail_view),
    path('', include('comment.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

