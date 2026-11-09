from django import template

register = template.Library()


@register.filter
def uk_pluralize(value, forms):
    """Choose the correct Ukrainian noun form from three comma-separated forms."""
    try:
        number = abs(int(value))
        singular, paucal, plural = (form.strip() for form in forms.split(","))
    except (TypeError, ValueError):
        return ""

    last_two_digits = number % 100
    last_digit = number % 10

    if 11 <= last_two_digits <= 14:
        return plural
    if last_digit == 1:
        return singular
    if 2 <= last_digit <= 4:
        return paucal
    return plural
