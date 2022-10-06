from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_XML, name='show_XML'),
    path('json/', show_JSON, name='show_JSON'),
    path('json/<int:id>', show_JSON_by_id, name='show_JSON_by_id'),
    path('xml/<int:id>', show_XML_by_id, name='show_XML_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('ajax/add/', add_wishlist_ajax, name='add_wishlist_ajax'),
]