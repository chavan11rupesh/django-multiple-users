from django.contrib import admin
from .models import Form

# Register your models here.
class FormAdmin(admin.ModelAdmin):

    def get_fields(self, request, obj=None):
        fields = super(FormAdmin, self).get_fields(request, obj)
        groups = request.user.groups.all()
        is_group_2 = [True for i in groups if i.name == "group2"]
        is_super = request.user.is_superuser
        if is_super and is_group_2 :
            fields = ('principal_name',)
        else:
            fields = ('teacher_name',)
        return fields

admin.site.register(Form, FormAdmin)
