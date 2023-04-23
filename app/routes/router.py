# from django.urls import path, re_path
from rest_framework.routers import SimpleRouter
from app.views import UserViewset
from app.auth.auth_views import AuthLogin, Authsignup, Authrefresh


router = SimpleRouter()
router.register("users", UserViewset)
router.register("signin", AuthLogin, basename="signin")
router.register("signup", Authsignup, basename="signup")
router.register("refresh", Authrefresh, basename="refresh")

urlpatterns = [
    *router.urls
]
