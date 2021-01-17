from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('Department', views.Department, name='Department'),
    path('Program', views.Program, name='Program'),
    path('Course', views.Course, name='Course'),
    path('Teacher', views.Teacher, name='Teacher'),
    path('Assign', views.assign,name='assign'),

    path('t_homepage/viewD/', views.viewD, name='viewD'),
    path('t_homepage/viewT/', views.viewT, name='viewT'),
    path('t_homepage/viewCl/', views.viewCl, name='viewCl'),
    path('t_homepage/viewCo/', views.viewCo, name='viewCo'),
    path('t_homepage/viewAs/', views.viewAs, name='viewAs'),

    path('t_homepage/viewD/<slug:dept_id>/EditD/', views.EditD, name='EditD'),
    path('t_homepage/viewT/<slug:teacher_id>/EditT/', views.EditT, name='EditT'),
    path('t_homepage/viewCl/<slug:program_id>/EditCl/', views.EditCl, name='EditCl'),
    path('t_homepage/viewCo/<slug:course_id>/EditCo/', views.EditCo, name='EditCo'),
    path('t_homepage/viewAs/<slug:id>/EditAs/', views.EditAs, name='EditAs'),

    path('t_homepage/viewD/<slug:dept_id>/deleteD/', views.deleteD, name='deleteD'),
    path('t_homepage/viewD/<slug:program_id>/deleteD/', views.deleteCl, name='deleteCl'),
    path('t_homepage/viewD/<slug:teacher_id>/deleteD/', views.deleteT, name='deleteT'),
    path('t_homepage/viewD/<slug:course_id>/deleteCo/', views.deleteCo, name='deleteCo'),

    path('homepage/timetable1/', views.timetable1, name='timetable1'),
    path('homepage/timetable2/', views.timetable2, name='timetable2'),
    path('homepage/timetable3/', views.timetable3, name='timetable3'),
    path('homepage/timetable4/', views.timetable4, name='timetable4'),

    ]