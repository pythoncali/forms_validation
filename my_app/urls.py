from django.conf.urls import url
from .views import my_view, my_better_view, my_csv_display

urlpatterns = [
    url(r'^$', my_view),
    url(r'^server-validation/$', my_better_view),
    url(r'^csv_display/$', my_csv_display),
]
