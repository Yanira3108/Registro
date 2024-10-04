from rest_framework.routers import DefaultRouter
from apps.registro.api.views import RegApiView

router_post = DefaultRouter()
router_post.register(prefix="posts", basename="posts", viewset=RegApiView)