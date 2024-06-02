from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserRegisterView(GenericAPIView):
    permission_classes = (AllowAny, )

