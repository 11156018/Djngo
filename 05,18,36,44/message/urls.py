"""
URL configuration for message project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from my.views import hello, homepage, list_posts, ntub, ntut, ntuh, ntust, others, mood, tech, note, urltest, message_list, signup, logout, edit_message, delete_message, edit_profile , post_detail # type: ignore
urlpatterns = [
    # www.xxx.com// -> 函數
    path('',hello),
    path('homepage', homepage, name='homepage.html'),

    path('ntub/', ntub, name='ntub.html'),
    path('ntut/', ntut, name='ntut.html'),
    path('ntuh/', ntuh, name='ntuh.html'),
    path('ntust/', ntust, name='ntust.html'),
    path('others/', others, name='others.html'),
    path('mood/', mood, name='mood.html'),
    path('tech/', tech, name='tech.html'),
    path('note/', note, name='note.html'),

    path('listposts/', list_posts),
    path('urltest/<int:year>/<int:month>/<str:words>/', \
        urltest, name='url-test'),

    path('admin/', admin.site.urls),
    path('post/<slug:slug>/', post_detail, name='post_detail.html'),

    # 用戶認證
    path('signup/', signup, name='signup.html'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # 留言管理
    path('message/edit/<int:message_id>/', edit_message, name='edit_message'),
    path('message/delete/<int:message_id>/', delete_message, name='delete_message'),
    path('messages/', message_list, name='message_list.html'),
    path('edit_profile', edit_profile, name='edit_profile.html'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

