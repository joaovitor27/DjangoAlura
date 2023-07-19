from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Photography(models.Model):
    CATEGORY_CHOICES = [
        ('NEBULA', 'Nebulosa'),
        ('GALAXY', 'Galáxia'),
        ('PLANET', 'Planeta'),
        ('STAR', 'Estrela'),
    ]

    name = models.CharField(_('Nome'), max_length=150, null=False, blank=False)
    subtitle = models.CharField(_('Legenda'), max_length=150, null=False, blank=False)
    category = models.CharField(_('Categoria'), max_length=8, choices=CATEGORY_CHOICES, default='')
    description = models.TextField(_('Descrição'), null=False, blank=False)
    image = models.ImageField(_('Imagem'), upload_to='images/%Y/%m/%d/', null=False, blank=True)
    published = models.BooleanField(_('Publicado'), default=True)
    user = models.ForeignKey(to=User, verbose_name=_('Usuário'), on_delete=models.SET_NULL, null=True, blank=False,
                             related_name='photography_user')
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Fotografia')
        verbose_name_plural = _('Fotografias')

    def __str__(self):
        return f'{self.name}'
