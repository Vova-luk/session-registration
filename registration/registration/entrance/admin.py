# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import Reg
#
#
# class CustomUserAdmin(UserAdmin):
#     model = Reg
#     list_display = ('email', 'first_name', 'last_name', 'patronymic', 'is_staff', 'is_active')
#     list_filter = ('is_staff', 'is_active')
#     ordering = ('email',)  # Указываем, что будем сортировать по email вместо username
#     # fieldsets = UserAdmin.fieldsets + (
#     #     (None, {'fields': ('patronymic',)}),
#     # )
#     # add_fieldsets = UserAdmin.add_fieldsets + (
#     #     (None, {'fields': ('patronymic',)}),
#     # )
#
#     # Удаляем username из методов, где он может использоваться
#     def get_queryset(self, request):
#         return super().get_queryset(request).select_related('patronymic')
#
#
# admin.site.register(Reg, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Reg

class CustomUserAdmin(UserAdmin):
    model = Reg
    list_display = ('email', 'first_name', 'last_name', 'patronymic', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)

    # Удаляем username из fieldsets
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'patronymic')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    # Удаляем username из add_fieldsets
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'patronymic', 'is_active', 'is_staff')}
        ),
    )

admin.site.register(Reg, CustomUserAdmin)
