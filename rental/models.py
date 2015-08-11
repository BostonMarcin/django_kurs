from django.db import models
from django.contrib.auth.models import User
from shelf.models import BookItem

from django.utils.timezone import now


# Create your models here.

class Rental():
    who = models.ForeignKey(User)
    when = models.DateTimeField(default=now)
    what = models.ForeignKey(BookItem)
    returned = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "Borrower: {0}, Book: {1} Borrow Date :{2}, Return Date {3}".format(self.who, self.what, self.when,
                                                                                   self.returned)
