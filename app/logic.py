def validate_all(self, query):
    lst = []
    for k, v in query.items():
        try:
            lst.append(validators[v](k))
        except ValidationError as e:
            print(e)
    return all(lst)


from rest_framework.exceptions import ValidationError
from tinydb import TinyDB, Query

from .validators import validate_phone, validate_date, validate_email, validate_text

validators = {
    'email': validate_email,
    'phone': validate_phone,
    'date': validate_date,
    'text': validate_text,
}


class IdentifyingCompletedForms:
    def get(self, request):
        """
        Return filtered data
        :param request:
        :type request:
        :return:
        :rtype:
        """
