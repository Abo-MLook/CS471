from django.contrib import admin
from .models import Female , Male ,Product,User,Watcher,Video
# Register your models here.
admin.site.register(Female)
admin.site.register(Male)
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Watcher)
admin.site.register(Video)