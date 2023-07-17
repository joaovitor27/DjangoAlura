from django.db import models
from django.utils.translation import gettext_lazy as _


class Photography(models.Model):
    name = models.CharField(_('Nome'), max_length=150, null=False, blank=False)
    subtitle = models.CharField(_('Legenda'), max_length=150, null=False, blank=False)
    description = models.TextField(_('Descrição'), null=False, blank=False)
    # image = models.ImageField(name=_('Imagem'), upload_to="images/")
    image = models.CharField(_('Imagem'), max_length=150, null=False, blank=False)
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Fotografia')
        verbose_name_plural = _('Fotografias')

    def __str__(self):
        return f'{self.name}'
