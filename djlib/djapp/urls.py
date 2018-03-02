from django.contrib.auth import views as auth_views
from django.conf.urls import url
#from .views import registration, home
from . import views


urlpatterns = [
    url(r'^login/', auth_views.login),
    url(r'^logout/', auth_views.logout, {'next_page': '/login/'}),
    url(r'^register/', views.registration),
    url(r'^$', views.home),
    #url(r'book/', views.BookView.as_view())
    url(r'book/', views.list_book)
]

