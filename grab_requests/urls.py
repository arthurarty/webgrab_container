"""
URL configuration for web_grab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from grab_requests.views import (
    GrabRequestListView, GrabRequestDetailView, GrabRequestBulkCreateView, GrabSettingListView, GrabSettingDetailView, UpdateSitePack
)


urlpatterns = [
    path('', GrabRequestListView.as_view(), name='home'),
    path('<int:pk>/', GrabRequestDetailView.as_view(), name='grab_detail_view'),
    path('bulk-create', GrabRequestBulkCreateView.as_view(), name='bulk_create'),
    path('settings', GrabSettingListView.as_view(), name='grab_settings'),
    path('settings/<int:pk>/', GrabSettingDetailView.as_view(), name='grab_settings_update'),
    path('update-site-pack', UpdateSitePack.as_view(), name='update_site_pack'),
]
