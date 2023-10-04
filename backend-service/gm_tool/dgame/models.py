from django.db import models

# Create your models here.

class gift(models.Model):
	gift_name = models.CharField(max_length=128)
	gift_id = models.CharField(max_length=10)

	def __unicode__(self):
		return self.gift_name