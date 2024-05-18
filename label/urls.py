from django.urls import path
from . import views
from django.urls import include, re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('members/', views.members, name='members'),
    path('music_bands/', views.music_bands, name='music_bands'),
    path('concert_halls/', views.concert_halls, name='concert_halls'),
    path('member_roles/', views.member_roles, name='member_roles'),
    path('concert_hall_contracts/', views.concert_hall_contracts, name='concert_hall_contracts'),
    path('concert_hall_managers/', views.concert_hall_managers, name='concert_hall_managers'),
    path('concert_programs/', views.concert_programs, name='concert_programs'),
    path('member_to_music_bands/', views.member_to_music_bands, name='member_to_music_bands'),
    path('music_band_contracts/', views.music_band_contracts, name='music_band_contracts'),
    path('members/edit/<int:members_id>/', views.edit_member, name='edit_member'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/delete/<int:members_id>/', views.delete_member, name='delete_member'),

]
