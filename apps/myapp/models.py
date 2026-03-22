from django.db import models

# Create your models here.
class Cousine(models.TextChoices):
    ITALY = 'italy', "Italy"
    FRENCH = 'french', 'French'
    UKRAINE = 'ukraine', 'Ulraine'


class MenuItem(models.Model):
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    couisine = models.CharField(max_length=20, choices=Cousine, default=Cousine.ITALY)

    def __str__(self):
        return f'{self.title} : {self.price}'

    class Meta:
        db_table = 'menu'
        verbose_name = 'menu'
        verbose_name_plural = 'menus'
        ordering = ['-price']
