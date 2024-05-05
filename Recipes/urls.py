from django.urls import path,include
from . import views
from .views import *

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('recipes/', views.recipes, name='recipes'),
    path('recipe/<int:pk>/', recipe, name='recipe'),
    path('add_recipe/', add_recipe, name="add_recipe"), 
    path('delete_recipe/<id>', delete_recipe, name = 'delete_recipe'),
    path('update_recipe/<id>', update_recipe, name = 'update_recipe'),
    path('list_recipe/', list_recipe, name="list_recipe"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()