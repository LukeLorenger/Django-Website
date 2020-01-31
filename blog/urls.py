from django.urls import path
from . import views # Imports views.py module

urlpatterns = [
    path('', views.home, name='blog-home'), # Path for home route
    # 3. program sees empty string, so it looks for pattern to match empty route^
    # 4. empty string pattern matches, will be handled by the function views.home^
    path('about/', views.about, name='blog-about'), # Path for about route
]