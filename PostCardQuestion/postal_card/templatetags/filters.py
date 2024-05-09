from django import template

register = template.Library()


@register.filter()
def change_number(text: str):
    # text amir khoobi 23 ali
    english_to_persian = {'0': '۰', '1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸',
                          '9': '۹'}
    output_string = ''.join(english_to_persian.get(c, c) for c in text)
    return output_string
