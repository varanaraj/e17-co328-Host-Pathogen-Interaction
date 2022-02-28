from django.contrib import admin
from .models import Collection, CSVFile
# Register your models here.

admin.site.register(Collection)
admin.site.register(CSVFile)
