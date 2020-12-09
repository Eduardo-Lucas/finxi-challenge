from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Peca, CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    fields = (
        "codigo", "descricao", "importada", "data_cadastro", "data_alteracao",
    )
    list_display = (
        "codigo", "descricao", "importada", "data_cadastro", "data_alteracao",
    )
    readonly_fields = (
        "data_cadastro", "data_alteracao"
    )
