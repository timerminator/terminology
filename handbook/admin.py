from django.contrib import admin
from .models import Handbook, ElementHandbook


class ElementHandbookAdmin(admin.ModelAdmin):
    search_fields = ('handbook_id',)
    list_display = ('code', 'handbook_id',)


admin.site.register(Handbook)
admin.site.register(ElementHandbook, ElementHandbookAdmin)
