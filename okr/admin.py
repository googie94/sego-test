from django.contrib import admin
from .models import Team, User, Objective, KeyResult, OkrProgress

admin.site.register(Team)
admin.site.register(User)

class KeyResultInline(admin.TabularInline):
	model = KeyResult
	extra = 0

class OkrProgressInline(admin.TabularInline):
	model = OkrProgress
	extra = 0

@admin.register(Objective)
class ObjectiveAdmin(admin.ModelAdmin):
	# list_display = ['id', 'title', 'goal', 'start_dt', 'end_dt']
	# fields = ['title', 'goal', 'start_dt', 'end_dt']
	list_display = ['id', 'title', 'team', 'create_date', 'end_date']
	# fields = ['']

	inlines = [
		KeyResultInline, 
		# OkrProgressInline
	]

@admin.register(KeyResult)
class KeyResultAdmin(admin.ModelAdmin):
	list_display = ['id', 'objective', 'title', 'percentage']

	inlines = [
		OkrProgressInline,
	]