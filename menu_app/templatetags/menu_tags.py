from django import template
from menu_app.models import Item

register = template.Library()


@register.inclusion_tag('menu/menu_template.html', takes_context=True)
def draw_menu(context, menu):
    """
    Рендерит меню на основе указанного названия `menu` из базы данных.
    Активный пункт меню определяется по значению параметра 'slug' в запросе.

    Параметры:
    - `context`: Контекст запроса Django.
    - `menu`: Название меню, которое нужно отрисовать.

    Возвращает словарь с древовидной структурой меню для включения в шаблон.

    Первый уровень вложенности - основные элементы меню, которые не имеют родителей.
    """
    active_slug = context['request'].GET.get('slug', None)
    # Извлекаем все элементы меню из базы данных, ровно за 1 запрос к БД.
    items = Item.objects.filter(menu__title=menu).select_related('parent')

    menu_items = {}  # Словарь для хранения элементов меню, сгруппированных по родителям.
    primary_items = []  # Основные элементы меню, у которых нет родителей.

    # Группируем элементы меню по их родителям.
    for item in items:
        menu_items.setdefault(item.parent_id, []).append(item)
        if item.parent_id is None:
            primary_items.append(item)

    def build_menu_tree(parent_id, active_slug):
        """
        Рекурсивно строит древовидную структуру меню для указанного родительского элемента.

        Параметры:
        - `parent_id`: ID родительского элемента меню.
        - `active_slug`: Значение параметра 'slug' активного пункта меню.

        Возвращает список дочерних элементов для указанного родителя.
        """
        children = menu_items.get(parent_id, [])
        child_items = []

        for child in children:
            is_active = child.slug == active_slug
            child_item = {
                'id': child.id,
                'title': child.title,
                'slug': child.slug,
                'child_items': build_menu_tree(child.id, active_slug),
                'is_active': is_active
            }
            child_items.append(child_item)

        return child_items

    # Строим древовидную структуру меню, начиная с корневых элементов (у которых нет родителей).
    menu_tree = build_menu_tree(None, active_slug)

    # Возвращаем словарь с построенной структурой меню.
    return {'items': menu_tree}
