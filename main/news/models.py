from django.db import models

# Create your table models for Data Base here.

# To create this model in DB you need to make migration
# to create migrations file use => python manage.py makemigrations

# To run migrations run python manage.py migrate

class Article(models.Model):
    title = models.CharField('Title', max_length=50)
    content = models.TextField('Content', blank=True) # blank means, is this field required

    # auto_now_add: save the date only one time at the creation
    created_at = models.DateTimeField('Creation date', auto_now_add=True)

    # auto_now: save the date each time when we updating the Article
    updated_at = models.DateTimeField('Updating date', auto_now=True)

    # upload_to: path to folder where we save our images
    image = models.ImageField('Image', upload_to='images/%Y/%m/%d/')
    is_published = models.BooleanField('Published', default=True)

    """
    __str__
    used to provide a string representation of a model object
    and when displaying model objects in the Django admin panel
    """
    def __str__(self):
        return self.title
    
    class Meta:
        # to see rigth names in admin
        verbose_name='Article'
        verbose_name_plural='Articles'
