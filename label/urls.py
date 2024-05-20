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

    path('concert_hall_contracts/edit/<int:concert_hall_contract_id>/', views.edit_concert_hall_contract, name='edit_concert_hall_contract'),
    path('concert_hall_contracts/create/', views.create_concert_hall_contract, name='create_concert_hall_contract'),
    path('concert_hall_contracts/delete/<int:concert_hall_contract_id>/', views.delete_concert_hall_contract, name='delete_concert_hall_contract'),

    path('concert_hall_managers/edit/<int:concert_hall_manager_id>/', views.edit_concert_hall_manager, name='edit_concert_hall_manager'),
    path('concert_hall_managers/create/', views.create_concert_hall_manager, name='create_concert_hall_manager'),
    path('concert_hall_managers/delete/<int:concert_hall_manager_id>/', views.delete_concert_hall_manager, name='delete_concert_hall_manager'),

    path('concert_halls/edit/<int:concert_hall_id>/', views.edit_concert_hall, name='edit_concert_hall'),
    path('concert_halls/create/', views.create_concert_hall, name='create_concert_hall'),
    path('concert_halls/delete/<int:concert_hall_id>/', views.delete_concert_hall, name='delete_concert_hall'),

    path('concert_programs/edit/<int:concert_program_id>/', views.edit_concert_program, name='edit_concert_program'),
    path('concert_programs/create/', views.create_concert_program, name='create_concert_program'),
    path('concert_programs/delete/<int:concert_program_id>/', views.delete_concert_program, name='delete_concert_program'),

    path('member_roles/edit/<int:member_roles_id>/', views.edit_member_role, name='edit_member_role'),
    path('member_roles/create/', views.create_member_role, name='create_member_role'),
    path('member_roles/delete/<int:member_roles_id>/', views.delete_member_role, name='delete_member_role'),

    path('member_to_music_bands/edit/<int:member_to_music_band_id>/', views.edit_member_to_music_band, name='edit_member_to_music_band'),
    path('member_to_music_bands/create/', views.create_member_to_music_band, name='create_member_to_music_band'),
    path('member_to_music_bands/delete/<int:member_to_music_band_id>/', views.delete_member_to_music_band, name='delete_member_to_music_band'),

    path('music_band_contracts/edit/<int:music_band_contract_id>/', views.edit_music_band_contract, name='edit_music_band_contract'),
    path('music_band_contracts/create/', views.create_music_band_contract, name='create_music_band_contract'),
    path('music_band_contracts/delete/<int:music_band_contract_id>/', views.delete_music_band_contract, name='delete_music_band_contract'),

    path('music_band/edit/<int:music_band_id>/', views.edit_music_band, name='edit_music_band'),
    path('music_band/create/', views.create_music_band, name='create_music_band'),
    path('music_band/delete/<int:music_band_id>/', views.delete_music_band, name='delete_music_band'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
