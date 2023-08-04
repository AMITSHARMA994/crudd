from django.contrib import admin
from django.urls import path
from mainapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),
    path('add/',views.addpage),
    path('delete/<int:num>/',views.deletePage),
    path('update/<int:num>/',views.updatePage),
    path('search/',views.searchPage),
]
