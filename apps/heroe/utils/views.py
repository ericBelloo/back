
# os
import csv
# Django
from django.http import HttpResponse
# Models
from apps.heroe.models import Heroes, Editorial


def create_heroes(request):
    with open('static/csv/heroe/heroes.csv') as object_csv:
        render_cvs = csv.reader(object_csv, delimiter='|', quotechar=' ')
        count = 0
        for row in render_cvs:
            obj_edit, create_edit = Editorial.objects.update_or_create(
                name=row[3]
            )
            obj_heroe, create_heroe = Heroes.objects.update_or_create(
                name=row[0],
                description=row[1],
                apparition=row[2],
                editorial=obj_edit,
            )
            if create_heroe:
                count += 1
        return HttpResponse(f'Se crearon { count } registros')
