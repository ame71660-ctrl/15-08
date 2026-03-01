from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView  # импортируем RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Редирект с пустого пути на /dashboard/
    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),

    # Подключаем все остальные пути приложения
    path('', include('main.urls')),
]
