from django import forms
from myapp.models import Blog

class Edit_blog(forms.ModelForm):
    class Meta:
        model = Blog
        fields=('title','desc')

        