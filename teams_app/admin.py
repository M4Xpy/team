from django.contrib import admin

from . import models

for model in (
    models.Team,
    models.Person,
):
    admin.site.register(model)
