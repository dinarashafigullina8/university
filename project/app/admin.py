from django.contrib import admin

from app.models import Address, University, Teacher, Department


class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'house')


class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'surname2', 'birth', 'department')


admin.site.register(Address, AddressAdmin)
admin.site.register(University, UniversityAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Teacher, TeacherAdmin)
