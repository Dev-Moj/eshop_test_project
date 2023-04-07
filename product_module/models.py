from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse


class productCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')


class product(models.Model):
    category = models.ForeignKey(productCategory, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=300)
    prise = models.IntegerField()
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], default=0)
    short_description = models.CharField(max_length=360, null=True)
    is_active = models.BooleanField(default=False)
    slug = models.SlugField(default='', null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absulote_url(self):
        return reverse('item_list', args=[self.slug])

    def __str__(self):
        return f'{self.title}:{self.prise}'
