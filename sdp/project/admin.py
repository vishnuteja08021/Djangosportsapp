from django.contrib import admin

# Register your models here.
from .models import Feedback, NormalPay,profile

admin.site.register(Feedback)
admin.site.register(NormalPay)
admin.site.register(profile)