from django import template

register = template.Library()

censor_list = ['блин,', 'блин', 'хреново,', 'хреново', 'пипец,', 'пипец', 'дерьмо,', 'дерьмо' ]


@register.filter()
def censor(value):

    if not isinstance(value, str):
        raise TypeError(f"unresolved type '{type(value)}' expected type 'str'")

    for word in value.split():
        if word.lower() in censor_list:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return value
