from django.urls import path

from menu_app.views import IndexPageView


app_name = 'menu_app'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index')
]