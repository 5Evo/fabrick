from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Status)
admin.site.register(Tag)
admin.site.register(MobileCode)
admin.site.register(Mailing)
admin.site.register(Client)
admin.site.register(Message)

