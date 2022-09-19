from django.contrib import admin
from .models import State, Quote,Fact, FAQ

# Register your models here.
admin.site.register(State)
admin.site.register(Quote)
admin.site.register(FAQ)
admin.site.register(Fact)