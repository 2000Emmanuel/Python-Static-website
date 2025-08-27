from django.contrib import admin
from .models import Project, Skill, Experience, Education, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_date']
    list_filter = ['featured', 'created_date']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['featured']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']
    search_fields = ['name', 'category']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date']
    list_filter = ['start_date', 'company']
    search_fields = ['position', 'company', 'description']

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_date', 'end_date']
    list_filter = ['start_date', 'institution']
    search_fields = ['degree', 'institution', 'field_of_study']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_date']
    list_filter = ['created_date']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_date']
