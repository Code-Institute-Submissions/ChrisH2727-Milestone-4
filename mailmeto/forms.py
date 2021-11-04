from django import forms
from .models import RequestImage


class RequestForm(forms.ModelForm):
    """
    Sets up the image reponseform
    """

    class Meta:
        model = RequestImage
        fields = (
            'request_name',
            'request_email',
            'category',
            'description',
            )