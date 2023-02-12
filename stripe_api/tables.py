from pathlib import Path

from django_tables2 import tables, TemplateColumn
from .models import Item

template_path = str(Path('templates/table_raw.html').absolute())


class PriceTable(tables.Table):
    class Meta:
        model = Item
        attrs = {'class': 'table table-sm'}
        fields = ['name', 'description', 'price']

    edit = TemplateColumn(template_name=template_path, orderable=False)
