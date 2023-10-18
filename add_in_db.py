import os
import django
from menu_app.models import Menu, Item

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

menu = Menu.objects.create(title="Menu 8")

# Создаем элементы меню с 10 уровнями вложенности
parent_item = None
for i in range(1, 11):
    item = Item.objects.create(menu=menu, title=f"Item {i}b", parent=parent_item, slug=f"item{i}b")
    parent_item = item
