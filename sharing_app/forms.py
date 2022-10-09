from django import forms
from django.core.validators import FileExtensionValidator

from sharing_app.models import ShareFile, FileLink


class FileLinkForm(forms.ModelForm):
    class Meta:
        model = FileLink
        fields = "__all__"


class FileSharingForm(forms.Form):
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),
                            validators=[FileExtensionValidator(allowed_extensions=["pdf", "jpeg", "jpg", "png", "zip"],
                                                               message='Only "pdf", "jpeg", "jpg", "png", "zip" are '
                                                                       'acceptable.')])
