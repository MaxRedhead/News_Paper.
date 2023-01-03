from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter
from .models import Post, Category, Author
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'title': ['contains'],
            'categoryTypes': ['exact'],
            #'category': ['exact'],

        }

    author = ModelChoiceFilter(
        field_name='author',
        queryset=Author.objects.all(),
        label='Автор',
        empty_label='Все'
    )

    category = ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Все'
    )

    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Новость добавлена после',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}
        )
    )

    added_earlier = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='lt',
        label='Новость добалвена ранее',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'}
        )
    )
