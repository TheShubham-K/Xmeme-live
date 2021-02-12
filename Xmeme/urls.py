from django.urls import path, include
from . import views

urlpatterns = [

     # get and post req. for insert operation.
    path('memes-form/', views.memes_form, name='memes_insert'),
    
    # get and post req. for update operation.
    path('memes-update/<int:id>/', views.memes_form, name='memes_update'),

    # get req. to retrieve and display all records.
    path('', views.memes_List, name='memes_List'), 

    # to get JSON of the all id field.
    path('memes/', views.memes_json_all, name='meme_json_all'), 

    # to get JSON of the desired id field.
    path('memes/<int:id>/', views.memes_json, name='meme_json'),    
    
    # post req. to delete a meme using it's id
    path('delete/<int:id>/',views.memes_delete,name='memes_delete')

]