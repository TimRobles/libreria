from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Editorial(models.Model):
    RazonSocial = models.CharField(
        'Razón Social',
        max_length=120,
        help_text='Razón social registrada en SUNAT',
    )
    Ruc = models.BigIntegerField(
        'RUC',
    )
    Direccion = models.CharField(
        'Dirección',
        max_length=255,
        blank=True,
        null=True,
    )
    slug = models.SlugField(editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.RazonSocial)
        super(Editorial, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'

    def __str__(self):
        return self.RazonSocial
