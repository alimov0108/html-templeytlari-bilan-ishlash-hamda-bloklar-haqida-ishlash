from django.contrib import admin
from django.urls import path
from core.views import BirbaloView, ContactView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('birbalo/', BirbaloView.as_view()),
    path('contact/', ContactView.as_view()),
]
