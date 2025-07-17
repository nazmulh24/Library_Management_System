from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Member


class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name = "Additional Personal Info"
    fk_name = "user"


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("email", "first_name", "last_name", "is_active")
    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal Info",
            {"fields": ("first_name", "last_name")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )

    search_fields = ("email",)
    ordering = ("email",)
    inlines = (MemberInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)


admin.site.register(User, CustomUserAdmin)
