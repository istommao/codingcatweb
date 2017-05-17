"""extensions templatetags extags."""
from django import template

register = template.Library()    # pylint: disable=C0103


@register.assignment_tag
def activelink(reqpath, url):
    """activelink."""
    return 'activeLink' if reqpath.startswith(url) else ''
