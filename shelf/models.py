from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Author(models.Model):

    first_name = models.CharField(verbose_name=_("first name"), max_length=20)
    last_name = models.CharField(verbose_name=_('last_name'), max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = _('atuhor')
        verbose_name_plural = _('authors')

class Publisher(models.Model):

    name = models.CharField(max_length=70)

    def __str__(self):

        return self.name

class BookCategory(models.Model):

    name = models.CharField(max_length= 50)

    def __str__(self):

        return self.name

class Book(models.Model):

    #like manusript

    title = models.CharField(max_length= 100)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(BookCategory)

    def __str__(self):

        return self.title

class BookEdition(models.Model):

    book = models.ForeignKey(Book)
    isbn = models.CharField(max_length= 17)
    date = models.DateField()
    publisher = models.ForeignKey(Publisher)

    def __str__(self):

        return "[book.title],[publisher.name]".format(book = self.book, publisher = self.publisher )

COVER_TYPES = (
    ('soft', 'Soft'),
    ('hard', 'Hard'),
    #(value in database, display values)
)

class BookItem(models.Model):
    "Specimen"
    edition = models.ForeignKey(BookEdition)
    catalogue_number = models.CharField(max_length=38)
    cover_type = models.CharField(max_length= 4, choices=COVER_TYPES)

    def __str__(self):
        return "[edition], [cover]".format(edition = self.edition, cover = self.get_cover_type_display())

