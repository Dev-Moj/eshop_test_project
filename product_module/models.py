from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse


class producttag(models.Model):
    tag = models.CharField(max_length=200, verbose_name='عنوان ')

    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'

    def __str__(self):
        return self.tag


class productCategory(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, verbose_name='عنوان در url')

    def __str__(self):
        return f'{self.title}:{self.url_title}'

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی  ها'


class productinformation(models.Model):
    color = models.CharField(max_length=200, verbose_name='رنگ')
    size = models.CharField(max_length=200, verbose_name='سایز')

    def __str__(self):
        return f'({self.color}:{self.size})'

    class Meta:
        verbose_name = 'اطلاعات تکمیلی'
        verbose_name_plural = 'تمامی اطلاعات تکمیلی'


class product(models.Model):
    category = models.ForeignKey(productCategory, on_delete=models.CASCADE, null=True, verbose_name='دسته بندی',
                                 related_name='product')
    product_information = models.OneToOneField('productinformation', on_delete=models.CASCADE,
                                               related_name='product_information', verbose_name='اطلاعات تکمیلی',
                                               null=True, blank=True)
    product_tag = models.ManyToManyField(producttag, verbose_name='تگ های محصولات')
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

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
