from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', views.post_home, name='post_home'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/new/', views.post_new, name = 'post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('contact/', views.contact, name = 'contact'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name = 'post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('cs/', views.post_cs, name='post_cs'),
    path('art/', views.post_art, name='post_art'),
    path('pencils/', views.post_pencils, name='post_pencils'),
    path('acrylics/', views.post_acrylics, name='post_acrylics'),
    path('watercolours/', views.post_watercolours, name='post_watercolours'),
    path('oilpaints/', views.post_oil, name='post_oil'),
    path('digital/', views.post_digital, name='post_digital'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
