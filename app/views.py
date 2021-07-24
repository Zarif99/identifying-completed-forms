from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .logic import IdentifyingCompletedForms


class FormView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        identifying_completed_forms = IdentifyingCompletedForms()
        data = identifying_completed_forms.get(request)
        return Response(data=data)
