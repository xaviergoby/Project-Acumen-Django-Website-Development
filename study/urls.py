from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('grind', views.grind, name="grind"),
    path('knowledge-base', views.knowledge_base, name="knowledge_base"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('test_view', views.test_view, name="test_view"),
    # path('test-view', views.test_view, name="test_view"),
]
