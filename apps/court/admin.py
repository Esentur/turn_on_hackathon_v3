from django.contrib import admin

from apps.court.models import Court

class CourtInAdmin(admin.ModelAdmin):
    list_display = ['court_num', 'is_booked', 'customer', 'schedule']
    search_fields = ['court_num', 'schedule']
    list_filter = ['court_num','schedule']

admin.site.register(Court,CourtInAdmin)
