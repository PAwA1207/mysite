from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('reg_page', TemplateView.as_view(template_name='reg_page.html')),
]
