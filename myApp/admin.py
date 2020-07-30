from django.contrib import admin

# Register your models here.
from .models import Grades,Students

#注册
class StudentsInfo(admin.TabularInline):
    model=Students
    extra=2


class GradesAdmin(admin.ModelAdmin):
    inlines = [StudentsInfo]
    #修改列属性
    list_display = ['pk','gname','gdate','ggirlnum','gboynum']
    list_filter = ['gname']
    #search_fields = []
    #list_per_page = []
    #修改表属性
    #fields = []
    #fieldsets = []

class StudentsAdmin(admin.ModelAdmin):
    def gender(self):
        if self.sgender:
            return "男"
        else:
            return "女"
    gender.short_description = "性别"
    list_display = ['pk','sname','sage',gender,'scontend','sgrade','isDelete']



admin.site.register(Grades, GradesAdmin)
admin.site.register(Students,StudentsAdmin)