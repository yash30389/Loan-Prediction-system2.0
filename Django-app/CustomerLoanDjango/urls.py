from django.contrib import admin
from django.urls import path, include
from myapi import views
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "LPS Admin"
admin.site.site_title = "LPS Admin Portal"
admin.site.index_title = "Welcome to Loan Prediction System"

urlpatterns = [
    path('', include('myapi.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)