from django.contrib import admin
from .models import Worker, SalesPoint, Visiting


class WorkerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ['name']


class SalesPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'worker')
    search_fields = ['name']


class VisitingAdmin(admin.ModelAdmin):
    list_display = ('sales_point', 'date', 'sales_point_name', 'sales_point_worker')
    readonly_fields = ('sales_point', 'date', 'sales_point_name', 'sales_point_worker', 'latitude', 'longitude')
    search_fields = ['sales_point__name', 'sales_point__worker__name']


    def sales_point_name(self, obj):
        return obj.sales_point.name


    def sales_point_worker(self, obj):
        return obj.sales_point.worker.name


    def has_add_permission(self, request):
        return False


    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Worker, WorkerAdmin)
admin.site.register(SalesPoint, SalesPointAdmin)
admin.site.register(Visiting, VisitingAdmin)
