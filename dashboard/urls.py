from django.urls import path


from .views import (
    dashboard,
    profile,
    messages,
    projects,

    )

app_name = 'dashboard'
urlpatterns = [

    path('', dashboard, name='dashboard'),

    path('messages/', messages, name='messages'),

    path('projects', projects, name='projects'),


]
