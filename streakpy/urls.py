from django.urls import path
from . import view
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .view import logout_view

urlpatterns = [
    path('', view.home, name='home'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('register/', view.register_view, name='register'),
path('habits/', view.habit_list, name='habit_list'),
path('logout/', logout_view, name='logout'),
path('add-habit/', view.add_habit, name='add_habit'),
    path('complete-habit/<int:habit_id>/', view.complete_habit, name='complete_habit'),
    path('delete-habit/<int:habit_id>/', view.delete_habit, name='delete_habit'),
    path('habit/<int:habit_id>/', view.habit_detail, name='habit_detail'),

]
