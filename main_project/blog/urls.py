from django.urls import path
from .views import *


urlpatterns = [
    path('', NewsHome.as_view(), name='home'),
    path('category/<int:cat_id>/', NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
]
