## Приложение Django Tree Menu
Это приложение Django реализует иерархическое древовидное меню в соответствии с указанными требованиями.

## Описание задачи
Задача состоит в создании Django-приложения, реализующего древовидное меню с учетом следующих условий:

1. Реализация через Template Tag: Меню должно быть реализовано с использованием тега шаблона.
2. Разворачивание Элементов Меню: Все элементы меню выше выделенного пункта должны быть развернуты. Первый уровень вложенности под выделенным пунктом также должен быть развернут.
3. Хранение в БД: Элементы меню должны храниться в базе данных.
4. Панель Администратора: Элементы меню должны быть редактируемы в панели администратора Django.
5. Активный Пункт Меню: Активный пункт меню должен определяться на основе URL текущей страницы.
6. Несколько Меню: На одной странице может существовать несколько меню. Они идентифицируются по своим названиям.
7. Поведение при Нажатии на Меню: При нажатии на элемент меню должно выполняться переход к указанному URL. URL может быть явно указан или определен через именованный URL.
8. Оптимизация Запросов к БД: Каждая операция отрисовки меню должна потреблять ровно один запрос к базе данных.
   
## Установка и Использование
### Клонирование репозитория:

```git clone https://github.com/Miki323/test_menu```

### Установка необходимых пакетов:

```pip install -r requirements.txt```

### Применение миграций:

```python manage.py migrate```

### Создание суперпользователя для доступа к панели администратора:

```python manage.py createsuperuser```

### Запуск сервера разработки:

```python manage.py runserver```

## Доступ к панели администратора Django:

```Перейдите по адресу http://localhost:8000/admin/, чтобы добавлять и управлять элементами меню.```

## Использование в шаблонах Django:

В своих шаблонах Django используйте тег шаблона draw_menu, чтобы отрисовать меню на основе его названия:

```
{% load menu_tags %}

<div class="menu">
  {% draw_menu 'main_menu' %}
</div>
```

Замените 'main_menu' на желаемое название меню.
