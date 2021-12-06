#{{ app_name }}/models.py
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Furnizor(models.Model):
    MONTH_CHOICES = (
        ("JANUARY", _("January"),
    )

    choices = models.CharField(verbose_name=_("nume adresa"),max_length=9, choices=MONTH_CHOICES, default="JANUARY")
    charfield = models.CharField(verbose_name=_("IBAN"), max_length=254, blank=True, null=True, default="")
    textfield = models.TextField(verbose_name=_("nume"), blank=True, max_length=250, null=True, default="")
    emailfield = models.EmailField(verbose_name=_("nume adresa"), max_length=254)
    tip_strada = models.ForeignKey(TipStrada, verbose_name=_("nume"), related_name="adresa", on_delete=models.CASCADE)
    soft_delete = models.BooleanField(verbose_name=_("Ascunde"), default=False)
    descriere = models.TextField(verbose_name=_("Descriere"), null=True, blank=True, default="")
    creat = models.DateTimeField(verbose_name=_("Dată creare"), auto_now_add=True, blank=True)
    actualizat = models.DateTimeField(verbose_name=_("Dată actualizare"), auto_now=True, blank=True)

    class Meta:
        verbose_name = "furnizor"
        verbose_name_plural = "furnizori"
        ordering = ["denumire"]

    def __str__(self):
        return self.denumire

    def get_absolute_url(self):
        return reverse("inventar:furnizor", args=[self.pk])



