#this file was created it did not come with django
#configuring url within application

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    #urls for the selling pages
    path('user-details/', views.user_details_view, name='user_details'),
    path('selling-progress/', views.selling_progress_view, name='selling_progress'),
    path("about-us/", views.aboutus, name="aboutus"),

    #   urls for the jewel items
    path('allitems/', views.all_items, name='all_items'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    # urls for the searchpatterns
    
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('search/', views.search_items, name='search_items'),

]



