from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'booktest/$',views.IndexView.as_view()),
    url(r'books/$',views.BookView.as_view()),
]