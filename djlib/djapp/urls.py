from django.contrib.auth import views as auth_views
from django.conf.urls import url
#from .views import registration, home
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('book_api', views.BookViewSet)

urlpatterns = [
    url(r'^login/', auth_views.login),
    url(r'^logout/', auth_views.logout, {'next_page': '/login/'}),
    url(r'^register/', views.registration),
    url(r'^$', views.home),
    #url(r'book/', views.BookView.as_view())
    url(r'book/', views.list_book),
    #url(r'book_api/', views.BookApiView.as_view()),
    #url(r'book_api/<int:id>/', views.BookDetailView.as_view())
]

urlpatterns += router.urls

