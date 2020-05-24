from django.conf.urls import url
from  django.urls import path
from . import views
app_name='index'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^faq/', views.faq, name='faq'),
    url(r'^pricing/', views.pricing, name='pricing'),
    url(r'^havenot/', views.havenot, name='havenot'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    path('delete/<int:id>/', views.user_delete, name='delete'),
    ]