from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import profile, logout_view

urlpatterns = [
    # Дашборд
    path('dashboard/', views.dashboard, name='dashboard'),

    # Уроки
    path('lessons/', views.lessons_view, name='lessons'),
    path('lessons/edit/<int:lesson_id>/', views.edit_lesson, name='edit_lesson'),
    path('lessons/delete/<int:lesson_id>/', views.delete_lesson, name='delete_lesson'),
    path('lessons/done/<int:lesson_id>/', views.mark_done, name='mark_done'),

    # Словарь
    path('vocabulary/', views.vocabulary, name='vocabulary'),
    path('add/', views.add_word, name='add_word'),

    # Календарь
    path('calendar/', views.my_calendar, name='calendar'),
    path('calendar/<int:year>/<int:month>/', views.my_calendar, name='calendar_by_month'),

    # Профиль
    path("profile/", profile, name="profile"),

    # Аутентификация
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register_view, name='register'),

    # Logout — используем только один путь
    path('logout/', logout_view, name='logout'),  # твой вариант с POST-logout
]




