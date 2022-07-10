from django.contrib import admin
from django import forms
from api.models import Email


class EmailAdmin(admin.ModelAdmin):
    """Settings for the Email class in Django admin"""

    readonly_fields = ("created_at", "updated_at")

    def get_form(self, request, obj=None, **kwargs):
        kwargs["widgets"] = {"message": forms.Textarea}
        return super().get_form(request, obj, **kwargs)


admin.site.register(Email, EmailAdmin)
