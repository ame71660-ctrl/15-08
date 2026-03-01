from django.contrib  import admin
from .models import Lesson, Question, Answer, Event, Word, Progress

admin.site.register(Lesson)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Event)
admin.site.register(Word)
admin.site.register(Progress)


