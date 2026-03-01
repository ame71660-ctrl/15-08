from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    lesson_balance = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Lesson(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    topic = models.CharField(max_length=100, blank=True)
    lesson_progress = models.IntegerField(default=0)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.date} {self.time})"




class UserCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"




class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.text} ({self.course.name})"


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} (Question: {self.question.text})"




class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} ({self.date} {self.time})"




class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='progress_entries'
    )
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.course.name}"




class Vocabulary(models.Model):
    english = models.CharField(max_length=100)
    russian = models.CharField(max_length=100)
    transcription = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.english




class Word(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    english = models.CharField(max_length=100)
    russian = models.CharField(max_length=100)
    transcription = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.english




class UserStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    xp = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)
    last_activity = models.DateField(null=True, blank=True)

    def add_xp(self, amount):
        self.xp += amount
        self.save()

    def calculate_level(self):
        return self.xp // 300

    def __str__(self):
        return f"{self.user.username} stats"





