from django.urls import path
from . import views




from django.contrib.sitemaps.views import sitemap
from .sitemaps import RoomMemberSitemap

sitemaps = {
    'roommembers': RoomMemberSitemap,
}

urlpatterns = [
    path('',views.lobby),
    path('room/', views.room),
    path('get_token/', views.getToken),
    path('create_member/',views.createMember),
    path('get_member/',views.getMember),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', views.robots),
]