from django.db import models

class WishPriority(models.Model):
	weight = models.PositiveSmallIntegerField()
	priotxt = models.CharField(max_length=125)

	class Meta:
		verbose_name = 'Priority of a wish'
		verbose_name_plural = 'Priorities of a wish'
	pass

class Wish(models.Model):
	priority = models.ForeignKey(WishPriority)
	wishcover = models.ImageField()
	wishtxt = models.TextField()
	wishisbn = models.CharField(max_length=120)
	visible = models.BooleanField()
	dtticrt = models.DateTimeField(auto_now_add=True)
	dttichg = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name = 'Wish'
		verbose_name_plural = 'Wishes'

	pass
