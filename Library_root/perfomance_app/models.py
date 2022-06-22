from django.db import models



class library_Model(models.Model):
    Booknumber = models.IntegerField() # bno = book_number
    Bookauthor = models.CharField(max_length=100)
    Bookname = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    def __str__(self):
        return self.Bookauthor