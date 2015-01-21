from django.db import models


class Shelf(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Drawer(models.Model):
    shelf = models.ForeignKey(Shelf)
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Pdf(models.Model):
    drawer = models.ForeignKey(Drawer)
    name = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to="pdf_files")

    def __unicode__(self):
        return self.name
