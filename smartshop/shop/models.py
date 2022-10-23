from django.db import models

# Model: Category
class Category(models.Model):
    
    # Fields
    name = models.CharField( max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)
    # Model Meta class
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    
    # String Method
    def __str__(self):
        return self.name 


# Model: Product
class Product(models.Model):
    
    # Fields
    category = models.ForeignKey(Category,
                                related_name='products',
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                                blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)

    # Model Meta class
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
    
    # To string Model methond
    def __str__(self):
        return self.name
    

     

