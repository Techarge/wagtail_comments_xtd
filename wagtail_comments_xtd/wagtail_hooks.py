from django.urls import reverse, path
from wagtail_comments_xtd import urls
from django.conf.urls import include
from wagtail.admin.menu import MenuItem
from django.utils.translation import gettext_lazy as _

try:
    from wagtail import hooks
except ImportError:  # fallback for Wagtail <4.2
    from wagtail.core import hooks


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        path("comments/", include(urls)),
    ]


@hooks.register('register_admin_menu_item')
def register_styleguide_menu_item():
    return MenuItem(
        _('Comments'),
        reverse('wagtail_comments_xtd_pages'),
        classnames='icon icon-fa-comments-o',
        order=1000
    )
