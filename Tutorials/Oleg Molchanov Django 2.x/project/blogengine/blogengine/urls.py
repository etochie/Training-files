
from django.contrib import admin
from django.urls import path
from django.urls import include

from .views import blog_redirect

urlpatterns = [
    path('', blog_redirect),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
