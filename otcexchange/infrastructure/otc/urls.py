from django.contrib import admin
from django.urls import path, include


urlpatterns_v2 = [
    path("account/", include("otcexchange.application.account.urls"))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v2/', include(urlpatterns_v2))
]
