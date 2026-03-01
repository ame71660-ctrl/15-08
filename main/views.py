from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from datetime import date, datetime
import calendar
import json

from .models import Word, Lesson, Event
from .forms import LessonForm, EventForm


def home_redirect(request):
    return redirect('login')


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not username or not email or not password or not password2:
            messages.error(request, "All fields are required")
        elif password != password2:
            messages.error(request, "Passwords do not match")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
        else:
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "Registration successful! You can log in now.")
            return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == "POST":
        username_or_email = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username_or_email, password=password)
        if not user:
            try:
                user_obj = User.objects.get(email=username_or_email)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Incorrect username/email or password")

    return render(request, "login.html")


from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def logout_view(request):
    if request.method == "POST":
        logout(request)  # разлогиниваем
        return redirect('login')
    return render(request, "logout.html")  # GET рендерит страницу с кнопкой



@login_required(login_url='login')
def dashboard(request):
    lessons = Lesson.objects.filter(user=request.user, date__gte=date.today()).order_by('date', 'time')
    next_lesson = lessons.first() if lessons.exists() else None
    return render(request, 'dashboard.html', {'next_lesson': next_lesson})


@login_required(login_url='login')
def lessons_view(request):
    topics = ['Grammar', 'Vocabulary', 'Reading', 'Listening', 'Speaking', 'Writing']

    if request.method == "POST":
        title = request.POST.get("title")
        lesson_date = request.POST.get("date")
        lesson_time = request.POST.get("time")
        topic = request.POST.get("topic")

        if title and lesson_date and lesson_time and topic:
            Lesson.objects.create(
                user=request.user,
                title=title,
                date=lesson_date,
                time=lesson_time,
                topic=topic
            )
            messages.success(request, "Lesson added successfully!")
            return redirect("lessons")
        else:
            messages.error(request, "All fields are required!")

    lessons = Lesson.objects.filter(user=request.user).order_by('date', 'time')

    context = {
        'lessons': lessons,
        'topics': topics,
        'today_date': date.today().isoformat()
    }
    return render(request, 'lessons.html', context)

@login_required(login_url='login')
def edit_lesson(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, user=request.user)
    if request.method == "POST":
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, "Lesson updated successfully!")
            return redirect('lessons')
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'edit_lesson.html', {'form': form})


@login_required(login_url='login')
def delete_lesson(request, lesson_id):
    if request.method == "POST":
        lesson = get_object_or_404(Lesson, id=lesson_id, user=request.user)
        lesson.delete()
        messages.success(request, "Lesson deleted successfully!")
    return redirect('lessons')


@login_required(login_url='login')
def mark_done(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id, user=request.user)
    lesson.done = True
    lesson.save()
    messages.success(request, "Lesson marked as done!")
    return redirect('lessons')


@login_required(login_url='login')
def vocabulary(request):
    words = Word.objects.all()
    return render(request, 'vocabulary.html', {'words': words})

@login_required(login_url='login')
def add_word(request):
    if request.method == "POST":
        english = request.POST.get("english")
        russian = request.POST.get("russian")
        transcription = request.POST.get("transcription")

        if english and russian:
            Word.objects.create(english=english, russian=russian, transcription=transcription)
            messages.success(request, "Word added successfully!")
        else:
            messages.error(request, "English and Russian are required!")

        return redirect("vocabulary")

    return render(request, "add_word.html")


def my_calendar(request, year=None, month=None):
    now = datetime.now()

    if year is None:
        year = now.year
    if month is None:
        month = now.month

    # Фильтр уроков по пользователю и выбранному месяцу/году
    lessons = Lesson.objects.filter(
        user=request.user,
        date__year=year,
        date__month=month
    )
    lessons_days = [lesson.date.day for lesson in lessons]

    # Расчёт предыдущего/следующего месяца и года для навигации
    prev_month = month - 1 or 12
    prev_month_year = year - 1 if month == 1 else year
    next_month = month + 1 if month < 12 else 1
    next_month_year = year + 1 if month == 12 else year
    prev_year = year - 1
    next_year = year + 1

    context = {
        "year": year,
        "month": month,
        "month_name": calendar.month_name[month],
        "lessons": lessons,
        "lessons_days": lessons_days,
        "today_day": now.day,
        "today_month": now.month,
        "today_year": now.year,
        "days_in_month": range(1, calendar.monthrange(year, month)[1] + 1),
        "empty_start": range(calendar.monthrange(year, month)[0]),
        "prev_year": prev_year,
        "next_year": next_year,
        "prev_month": prev_month,
        "prev_month_year": prev_month_year,
        "next_month": next_month,
        "next_month_year": next_month_year,
    }

    return render(request, "calendar.html", context)

@login_required(login_url='login')
def english_view(request):
    return render(request, 'english.html')


@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

from datetime import datetime, date
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lesson

def lessons(request):
    # Обработка формы добавления урока
    if request.method == "POST":
        title = request.POST.get("title")
        lesson_date = request.POST.get("date")
        lesson_time = request.POST.get("time")
        topic = request.POST.get("topic")

        # Проверка, что дата не в прошлом
        if lesson_date:
            lesson_date_obj = datetime.strptime(lesson_date, "%Y-%m-%d").date()
            if lesson_date_obj < date.today():
                messages.error(request, "❌ You cannot add a lesson in the past.")
                return redirect("lessons")

        # Создание урока
        Lesson.objects.create(
            title=title,
            date=lesson_date,
            time=lesson_time,
            topic=topic,
            user=request.user
        )

        messages.success(request, "✅ Lesson added successfully!")
        return redirect("lessons")

    # Список уроков текущего пользователя
    lessons_list = Lesson.objects.filter(user=request.user).order_by("date")

    # Отправка данных в шаблон
    return render(request, "lessons.html", {
        "lessons": lessons_list,
        "today_date": date.today().isoformat(),
        "now_time": datetime.now().strftime("%H:%M"),
        "topics": ["Grammar", "Vocabulary", "Reading"]  # пример тем
    })
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required  # проверяет, что пользователь вошёл в систему
def profile_view(request):
    user = request.user
    return render(request, 'main/profile.html', {'user': user})

from .forms import ProfileUpdateForm, LanguageForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, logout
from django.utils import translation
from .views import profile

@login_required
def profile(request):
    # --- обработка POST ---
    if request.method == 'POST':
        if 'update_profile' in request.POST:
            form = ProfileUpdateForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Profile updated!")
                return redirect('profile')
        elif 'change_password' in request.POST:
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, "Password changed!")
                return redirect('profile')
        elif 'change_language' in request.POST:
            lang = request.POST.get('language')
            translation.activate(lang)
            request.session['django_language'] = lang
            messages.success(request, "Language updated!")
            return redirect('profile')
        elif 'delete_account' in request.POST:
            request.user.delete()
            logout(request)
            return redirect('login')

    # --- GET и рендер ---
    form = ProfileUpdateForm(instance=request.user)
    password_form = PasswordChangeForm(request.user)
    language_form = LanguageForm()

    # --- вычисляем completed_lessons для шаблона ---
    completed_lessons = request.user.lesson_set.filter(done=True).count()

    # --- вычисление уровня ---
    if completed_lessons < 10:
        level, next_level = "A1", 10
    elif completed_lessons < 20:
        level, next_level = "A2", 20
    elif completed_lessons < 40:
        level, next_level = "B1", 40
    elif completed_lessons < 60:
        level, next_level = "B2", 60
    elif completed_lessons < 80:
        level, next_level = "C1", 80
    else:
        level, next_level = "C2", completed_lessons

    # --- прогресс ---
    progress = int((completed_lessons / next_level) * 100) if next_level > completed_lessons else 100

    return render(request, 'profile.html', {
        'form': form,
        'password_form': password_form,
        'language_form': language_form,
        'completed_lessons': completed_lessons,
        'level': level,
        'progress': progress
    })
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect

def login_auto_view(request):
    # Если уже авторизован — сразу на dashboard
    if request.user.is_authenticated:
        return redirect('dashboard')

    # Дефолтное имя пользователя (можно любое)
    username = "guest"

    # Проверяем, есть ли такой пользователь
    user, created = User.objects.get_or_create(username=username)

    # Логиним его
    login(request, user)

    # Редирект на dashboard
    return redirect('dashboard')

from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from .models import Lesson, Word, Progress


def dashboard(request):
    user = request.user

    # Total words
    total_words = Word.objects.filter(user=user).count()

    # Weekly words
    week_ago = timezone.now() - timedelta(days=7)
    weekly_words = Word.objects.filter(user=user, id__isnull=False).count()

    weekly_goal = 30
    progress_percent = int((weekly_words / weekly_goal) * 100) if weekly_words else 0

    # Next lesson
    next_lesson = Lesson.objects.filter(user=user, done=False).order_by("date", "time").first()

    # Completed lessons
    completed_lessons = Lesson.objects.filter(user=user, done=True).count()

    # Recent words
    recent_words = Word.objects.filter(user=user).order_by("-id")[:5]

    # Streak (простая версия)
    streak = completed_lessons

    context = {
        "total_words": total_words,
        "weekly_words": weekly_words,
        "weekly_goal": weekly_goal,
        "progress_percent": progress_percent,
        "next_lesson": next_lesson,
        "completed_lessons": completed_lessons,
        "recent_words": recent_words,
        "streak": streak,
        "xp": completed_lessons * 50,
        "level": (completed_lessons * 50) // 300,
    }

    return render(request, "dashboard.html", context)
