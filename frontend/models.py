from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Template(models.Model):
    name = models.CharField(verbose_name=_('name'), max_length=255)
    content = models.TextField(verbose_name=_('content'))
    status = models.BooleanField(verbose_name=_('status'), default=False)

    class Meta:
        verbose_name = _('template')
        verbose_name_plural = _('templates')


class Article(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'))
    title = models.CharField(verbose_name=_('title'), max_length=255)
    content = models.TextField(verbose_name=_('content'))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')