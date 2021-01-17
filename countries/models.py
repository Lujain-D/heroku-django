from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Continent(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'continents'
        app_label = 'continents'


class Country(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    iso3 = models.CharField(max_length=3)
    number = models.SmallIntegerField(max_length=3)
    continent = models.ForeignKey('countries.Continent', on_delete=models.SET_NULL, db_column="continent_code", null=True)

    class Meta:
        managed = False
        db_table = 'countries'
        app_label = 'countries'



#
# class Country(models.Model):
#
#     name = models.CharField(max_length=50)
#     full_name = models.CharField(max_length=100)
#     iso3 = models.CharField(max_length=3)
#     number = models.IntegerField(max_length=3)
#

  # `code` CHAR(2) NOT NULL ,
  # `name` VARCHAR(255) NOT NULL ,
  # `full_name` VARCHAR(255) NOT NULL ,
  # `iso3` CHAR(3) NOT NULL ,
  # `number` SMALLINT(3)  NOT NULL ,
  # `continent_code` CHAR(2) NOT NULL,
  # PRIMARY KEY (`code`),
  # FOREIGN KEY(continent_code) REFERENCES continents(code)
