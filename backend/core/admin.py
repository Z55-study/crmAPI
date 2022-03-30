from django.contrib import admin
from .models import Person


admin.site.site_header = 'Простой и доступный CRM'
admin.site.site_title = 'SimpleCRM '
admin.site.index_title = 'Добро пожаловать в Вашу CRM систему'


class PersonAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('full_name', 'position', 'chief', 'salary', 'information_salary')
    list_display_links = ('position', 'chief')
    list_filter = ('position', 'chief')

    actions = ['make_published']

    @admin.action(description='Удалить данные о ЗП')
    def make_published(self, request, queryset):
        queryset.update(information_salary=None)


admin.site.register(Person, PersonAdmin)

