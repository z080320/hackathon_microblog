from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from gtoext.rest import SuccessResponse
from gtoext.contrib.garena_oauth.user import AuthGarenaUser, PermitGarenaUser302, PermitGarenaUser

import logging
LOG = logging.getLogger("main")


class ProtectedTemplateView(APIView):
    template_name = ''

    renderer_classes = (TemplateHTMLRenderer, )
    authentication_classes = (AuthGarenaUser, )
    permission_classes = (PermitGarenaUser302, )

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        kwargs.update({'user': request.user})
        return SuccessResponse(kwargs, template_name=self.__class__.template_name)

class ProtectedBaseAPIView(APIView):
    authentication_classes = (AuthGarenaUser,)
    permission_classes = (PermitGarenaUser, )


