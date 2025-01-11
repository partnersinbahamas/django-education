from django.db import models
from django.urls import reverse_lazy

# Create your table models for Data Base here.

# To create this model in DB you need to make migration
# to create migrations file use => python manage.py makemigrations

# To run migrations run python manage.py migrate

class Article(models.Model):
    title = models.CharField('Title', max_length=50)
    content = models.TextField('Content', blank=True) # blank means, is this field required

    # auto_now_add: save the date only one time at the creation
    created_at = models.DateTimeField('Created', auto_now_add=True)

    # auto_now: save the date each time when we updating the Article
    updated_at = models.DateTimeField('Updated', auto_now=True)

    # upload_to: path to folder where we save our images
    image = models.ImageField('Image', upload_to='images/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField('Published', default=True)

    """
    models.ForeignKey is used to create a relationship between models,
    specifically to define a "one-to-many" relationship.
    This allows one record in one table (model) to be associated with multiple records in another table.

    Attrs:
        - to (first argument): Specifies the model to which the relationship is established. In the example above, it's Category.
        - on_delete: Determines what happens to the related records if the parent record is deleted.
            - models.CASCADE: Deletes related records.
            - models.PROTECT: Prevents deletion and raises an error.
            - models.SET_NULL: Sets the field to NULL.
            - models.SET_DEFAULT: Sets a default value.
            - models.SET(...): Sets a custom value or function.
            - models.DO_NOTHING: Does nothing.
        - related_name (optional): Specifies the name for the reverse relationship from the related model.
        - null (optional): determines whether this field can store a NULL value in the database, meaning whether it can be empty.

    to create relations ships you can use:
        - ForeignKey
        - ManyToManyField
    """
    category = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name="categories",
        null=True,
    )
    views = models.IntegerField(default=0)

    """
    __str__
    used to provide a string representation of a model object
    and when displaying model objects in the Django admin panel
    """
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse_lazy('view_article', kwargs={'article_id': self.pk})
        
    class Meta:
        # to see rigth names in admin
        verbose_name='Article'
        verbose_name_plural='Articles'
        # to sort element by in admin
        ordering = ['-created_at']

class Category(models.Model):
    # db_index set uniq index to the field
    name = models.CharField('Category name', max_length=50, db_index=True)

    def __str__(self):
        return self.name
    
    # get_absolute_url needs to redirect user after Article update, create in form
    # method is used to provide the absolute URL of an object.
    # It’s often defined in models to specify the path to a page associated with a particular instance of the model.
    def get_absolute_url(self):
        # args: path name from urls, args2 "id from urls": self.pk
        return reverse_lazy('category', kwargs={"pk": self.pk})

    class Meta:
        verbose_name='Category'
        verbose_name_plural='Categories'
        ordering=['pk']