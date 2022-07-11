from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class UrlStorage(models.Model):

    url_long = models.URLField(_('Url long'), max_length=2048)
    url_short = models.URLField(_('Url short'), max_length=256, unique=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_url',
        verbose_name=_('Owner'),
    )
    created = models.DateTimeField(_('Created date'), auto_now_add=True)

    class Meta:
        verbose_name = _('UrlStorage')
        verbose_name_plural = _('Films genre')
        constraints = [
            models.UniqueConstraint(
                fields=('owner', 'url_long'),
                name='owner_url_long',
            ),
        ]
