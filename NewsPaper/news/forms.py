from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    #title = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'categoryTypes',
            'author',
            'category',

        ]

    def clean(self):
        cleaned_data = super().clean()
        description = cleaned_data.get("title")
        if description is not None and len(description) < 10:
            raise ValidationError({
                "title": "Заголовк должен быть длиннее."
            })

        return cleaned_data

    def clean_title(self):
        title = self.cleaned_data["title"]
        if title[0].islower():
            raise ValidationError(
                "Заголовок должен начинаться с заглавной буквы"

            )

        #cleaned_data = super().clean()
        #description = cleaned_data.get("title")
       # if title == title:
            #raise ValidationError(
             #   "Такой заголовок уже используется."
           # )
        return title
