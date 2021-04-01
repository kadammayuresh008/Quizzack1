from user import views as user_views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path ,include
from blog import views as blog_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register, name="register"),
    path('quiz_page/',blog_views.quiz_page, name="quiz_page"),
    path('profile/',user_views.profile, name="profile"),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name="logout"),
    # path('',include('blog.urls')),
    path('',blog_views.home, name="home"),
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
