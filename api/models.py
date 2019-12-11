from django.db import models

class User(models.Model):
	"""
	Class to persist User data
	"""
	name = models.CharField(max_length=255, verbose_name="name")

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['name']


class Task(models.Model):
	"""
	Class to persist User Task data
	"""
	STATE_OPTIONS = (('to_do','To do'),('done','Done'))

	user = models.ForeignKey(User, verbose_name=u"User", on_delete=models.CASCADE)
	description = models.CharField(max_length=255, verbose_name="description")
	state = models.CharField(max_length=10, choices=STATE_OPTIONS)

	def __str__(self):
		return "%s - %s" % (self.description, self.user)

	class Meta:
		ordering = ['description']