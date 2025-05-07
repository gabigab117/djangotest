from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilisateur", related_name="addresses")
    address_line1 = models.CharField(max_length=255, verbose_name="Adresse 1")
    address_line2 = models.CharField(max_length=255, blank=True, verbose_name="Adresse 2")
    city = models.CharField(max_length=100, verbose_name="Ville")
    postal_code = models.CharField(max_length=20, verbose_name="Code postal")
    default = models.BooleanField(default=False, verbose_name="Adresse par défaut")

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"

    def __str__(self):
        return f"{self.address_line1}, {self.city}, {self.postal_code}"
    
    def save(self, *args, **kwargs):
        user_addresses = Address.objects.filter(user=self.user)
        
        if user_addresses.count() >= settings.MAX_ADDRESSES and self._state.adding:
            raise ValueError("Le nombre maximum d'adresses a été atteint.")
        
        if not user_addresses.exists():
            self.default = True
            
        super().save(*args, **kwargs)
