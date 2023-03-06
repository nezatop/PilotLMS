from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('create_course',views.create_course,name='create_course'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('<int:course_id>/update/', views.update_course, name='update_course'),
    path('<int:course_id>/delete/', views.delete_course, name='delete_course'),
    path('create_module/<int:course_id>/', views.create_module, name='create_module'),
    path('course/<int:course_id>/module/<int:module_id>/update/', views.update_module, name='update_module'),
    path('course/<int:course_id>/module/<int:module_id>/delete/', views.delete_module, name='delete_module'),
    path('<int:course_id>/modules/', views.course_modules, name='course_modules'),
    path('dashboard',views.dashboard,name='dashboard'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
