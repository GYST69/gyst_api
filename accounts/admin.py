from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
from django import forms


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("email",)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    list_display = ("email",)
    ordering = ("email",)

    fieldsets = ((None, {"fields": ("email", "password")}),)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password",
                    "is_superuser",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )

    filter_horizontal = ()


admin.site.register(Account, CustomUserAdmin)
