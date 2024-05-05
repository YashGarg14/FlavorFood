from django import template

register = template.Library()

@register.filter
def separate_instructions(text):
    lines = text.split('\n')
    result = '<ul style="max-width: 900px; text-align: justify;">'
    for line in lines:
        result += f'<li>{line.strip()}</li>'
    result += '</ul>'
    return result
