from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from proj1 import views



urlpatterns = [
    path('', views.home, name='home'),
    path('Register/',views.Register, name='Register'),
    path('profile/',views.profile, name='profile'),
    path('edit_profile/',views.edit, name='edit'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('view_categary/', views.categaryview.as_view(), name='categaryview'),
    path('update/<int:pk>/', views.updatecategary.as_view(), name='updatecategary'),
    path('delete/<int:pk>/',views.delete_cateview, name='delete_cateview'),
    path('view_brand/', views.viewbrand.as_view(), name='viewbrand'),
    path('view_subcategary/', views.subcategaryv.as_view(), name='subcategaryv'),
    path('update_subcategary/<int:pk>/', views.updatesubcate.as_view(), name='updatesubcate'),
    path('delete_subcategary/<int:pk>/', views.Deletesubcate, name='Deletesubcate'),
    path('add_categary/', views.add_categary, name='add_categary'),
    path('add_brand/', views.add_brand, name='add_brand'),
    path('add_subcategary/', views.add_subcategary, name='add_subcategary'),
    path('delete_brand/<int:pk>/', views.Deletebrand, name='Deletebrand'),
    path('add_catalog/', views.add_catalog, name='add_catalog'),
    path('view_catalog/', views.catalogview.as_view(), name='catalogview'),
    path('add/', views.addcatlog, name='addcatlog'),

    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
