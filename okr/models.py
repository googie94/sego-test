from django.db import models
from django.db.models import Sum
from django.utils import timezone
###################

#okr team
class Team(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

#okr user
class User(models.Model):
	name = models.CharField(max_length=20)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='user')

	def __str__(self):
		return self.name

#class Objective
class Objective(models.Model):
	CHALLENGE = '0'
	NECESSARY = '1'
	PERSONAL = '2'
	TYPE_DATA_CHOICES=(
			('0', 'Challenge'),
			('1', 'Necessary'),
			('2', 'Personal')
	)
	TYPE_CHOICES = (('int', '정수'), ('float', '실수'), ('percent', '백분율'))
#############
	title = models.CharField(max_length=200)
	rate = models.FloatField()
	data_type = models.CharField(max_length=15, choices=TYPE_CHOICES)
	team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='objective_team')
	leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='objective_leader')
	type = models.CharField('Type', max_length=1, choices=TYPE_DATA_CHOICES, default=NECESSARY)
	create_date = models.DateField()
	end_date = models.DateField()

	def __str__(self):
		return self.title

#okr KeyResult
class KeyResult(models.Model):
	POSITIVE = '0'
	NEGATIVE = '1'
	BINARY = '2'
	TYPE_DATA_CHOICES = (
		('0', 'Positive'),
		('1', 'Negative'),
		('2', 'Binary')
	)
#################
	objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name='keyresult')
	title = models.CharField(max_length=200)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='objective_user')
	type_data = models.CharField('Type',
								 max_length=1,
								 choices=TYPE_DATA_CHOICES,
								 default=POSITIVE)
	obtained = models.FloatField(default=0)
	expected = models.FloatField()
	percentage = models.FloatField()
	create_date = models.DateField('publication date', auto_now_add=True)

	def save(self, *args, **kwargs):
		self.percentage = calculate_percentage(self.type_data, self.obtained, self.expected)
		super(KeyResult, self).save(*args, **kwargs)

	def __str__(self):
		return self.title

# #okr progress
class OkrProgress(models.Model):
	progress = models.FloatField()
	memo = models.CharField(max_length=500)
	create_date = models.DateField(default=timezone.now,)
	key_result = models.ForeignKey(KeyResult, on_delete=models.CASCADE, related_name='okrprogress')

	def __str__(self):
		return ' '

def calculate_percentage(type_data, obtained, expected):
	# Round without decimals
	if type_data == KeyResult.POSITIVE:
		return 100 * obtained / expected
	elif type_data == KeyResult.NEGATIVE:
		return 100 * (1 - obtained / expected)
	elif type_data == KeyResult.BINARY:
		if obtained == 0:
			return 0
		else:
			return 100










