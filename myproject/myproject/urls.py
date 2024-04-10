from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static #EP10 ทำ static ทำ blogs
from django.conf import settings #EP10 ทำ static ทำ blogs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('maintenance.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='maintenance/login.html'),name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='maintenance/logout.html'),name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #EP10 ทำ static ทำ blogs
