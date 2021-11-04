from django.forms import ModelForm
from core.models import blog



class BlogForms(ModelForm):
    class Meta:
        model = blog
        fields = "__all__"