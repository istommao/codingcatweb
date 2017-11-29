"""extensions templatetags extags."""
from django import template

register = template.Library()    # pylint: disable=C0103


@register.assignment_tag
def activelink(reqpath, url):
    """activelink."""
    return 'activeLink' if reqpath.startswith(url) else ''


@register.assignment_tag
def active_url(reqpath, url):
    """activelink."""
    return 'nav-this' if reqpath.startswith(url) else ''
