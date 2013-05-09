from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class JobType(models.Model):
    Category = models.ForeignKey(Category)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Notice(models.Model):
    JobType = models.ForeignKey(JobType)
    CompanyName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    EmailAddress = models.CharField(max_length=150)
    Mobile = models.CharField(max_length=15)
    LandLine = models.CharField(max_length=15)

    def __unicode__(self):
        return self.JobType.name + " " + self.CompanyName + " " + self.FirstName + " " + self.LastName

    def name(self):
        return (self.FirstName + " " + self.LastName).strip()
