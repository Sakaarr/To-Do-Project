from django.urls import path 
from . import views
urlpatterns = [
    path('' , views.addanddisplay , name='addanddisplay'),
    path('delete/<int:id>' , views.delete_data , name='delete'),
    path('<int:id>/' , views.update_data , name='update'),
]
