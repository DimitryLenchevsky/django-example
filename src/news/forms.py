from .models import Articles
from django.forms import ModelForm, TextInput, Textarea


class CreateArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ('title', 'body', 'date')