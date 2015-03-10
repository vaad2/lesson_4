from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User
from django.db.models import Q

from .models import Template, Article


class SuperAdminSite(AdminSite):
    def has_permission(self, request):
        return request.user.is_superuser and request.user.is_active and request.user.is_staff
        # return request.user.is_active and request.user.is_staff


admin_super = SuperAdminSite(name='admin_super')

admin_super.register(Group, GroupAdmin)
admin_super.register(User, UserAdmin)

admin_super.register(Template, list_display=['id', 'name', 'status'], list_editable=['name', 'status'])
admin_super.register(Article, list_display=['id', 'user', 'title'], list_editable=['user', 'title'])


class EditorAdminSite(AdminSite):
    def has_permission(self, request):
        return request.user.groups.filter(
            Q(name='editor') | Q(name='super_editor')).exists() and \
               request.user.is_active and request.user.is_staff


class AdminEditortMixin(admin.ModelAdmin):
    exclude = ['user']

    def get_queryset(self, request):
        qset = super(AdminEditortMixin, self).queryset(request)

        if request.user.groups.filter(name='super_editor').exists():
            return qset

        return qset.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class ArticleAdmin(AdminEditortMixin, admin.ModelAdmin):
    pass


admin_editor = EditorAdminSite(name='admin_editor')

admin_editor.register(Article, ArticleAdmin)

