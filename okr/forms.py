from django import forms
from .models import Team, User, Objective, KeyResult, OkrProgress

class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ('name',)

	def __init__(self, *args, **kwargs):
		super(TeamForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'inputFull height250 mb10'

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('name', 'team')

	def __init__(self, *args, **kwargs):
		super(UserForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'inputFull height250 mb10'

class ObjectiveForm(forms.ModelForm):
	# title = models.CharField(max_length=200)
	# rate = models.FloatField()
	# data_type = models.CharField(max_length=15, choices=TYPE_CHOICES)
	# team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='objective_team')
	# leader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='objective_leader')
	# type = models.CharField('Type', max_length=1, choices=TYPE_DATA_CHOICES, default=NECESSARY)
	# create_date = models.DateField()
	# end_date = models.DateField()

	class Meta:
		model = Objective
		fields = ('title', 'data_type', 'rate', 'team', 'leader', 'type', 'end_date')

	def __init__(self, *args, **kwargs):
		super(ObjectiveForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'inputFull height250 mb10'

	def clean(self):
		end_date = self.cleaned_data.get('end_date', None)

		# end_date >= create_date
		if end_date and (end_date < datetime.date.today()):
			self._errors['end_date'] = '마감일은 오늘 이후여야 해'
		return self.cleaned_data


class KeyResultForm(forms.ModelForm):

	# objective = models.ForeignKey(Objective, on_delete=models.CASCADE, related_name='keyresult')
	# title = models.CharField(max_length=200)
	# user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='objective_user')
	# type_data = models.CharField('Type',
	# 							 max_length=1,
	# 							 choices=TYPE_DATA_CHOICES,
	# 							 default=POSITIVE)
	# obtained = models.FloatField(default=0)
	# expected = models.FloatField()
	# percentage = models.FloatField()
	# create_date = models.DateField('publication date', auto_now_add=True)

	class Meta:
		model = KeyResult
		fields = ('title', 'user', 'type_data', 'obtained', 'expected', 'percentage')

	def __init__(self, *args, **kwargs):
		super(KeyResultForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'inputFull height250 mb10'

	def clean(self):
		obtained = self.cleaned_data.get('obtained', None)
		expected = self.cleaned_data.get('expected', None)
		type_data = self.cleaned_data.get('type_data', None)

		# obtained <= expected
		if ( obtained > expected ):
			self._errors['obtained'] = '획득이 기대보다 클 수 있을까?'
			# raise ValidationError('Obtained can not be greater than expected.')

		# if it's binary: obtained = 0 or 1 and expected = 1
		if ( type_data == KeyResult.BINARY ):
			if not (obtained == 0 or obtained == 1):
				self._errors['obtained'] = '획득은 0 이나 1 이여야 해'
				# raise ValidationError('Obtained must be 0 or 1.')

			if not (expected == 1):
				self._errors['expected'] = '기대는 1이여야만 해'
				# raise ValidationError('Expected must be 1.')

		return self.cleaned_data
	

class OkrProgressForm(forms.ModelForm):
	# progress = models.FloatField()
	# memo = models.CharField(max_length=500)
	# create_at = models.DateField(default=timezone.now,)
	# key_result = models.ForeignKey(KeyResult, on_delete=models.CASCADE, related_name='okrprogress')

	class Meta:
		model = OkrProgress
		fields = ('progress', 'memo')






















