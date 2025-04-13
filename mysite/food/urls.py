from . import views
from django.urls import path

##Make patterns or bring your views to this urls file and then take this file in project.urls file.

app_name = 'food'
urlpatterns = [
    # /food/
    path('',views.IndexClassView.as_view(),name='index'),
    # /food/1
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    # Additem
    path('add', views.CreateItem.as_view(),name='create_item'),
    # Edit items
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete items
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
    

]