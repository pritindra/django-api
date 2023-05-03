from django.db import models
from django.db import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()


class Employee(models.Model):
	__tablename__ = 'employee'
	name = models.CharField(max_length=40)
	position = models.CharField(max_length=20)
	department = models.CharField(max_length=20)
		
	def __str__ (self):
		return (str(self.id) + ': ' + self.name)
	
	