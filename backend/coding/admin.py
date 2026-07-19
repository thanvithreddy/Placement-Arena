from django.contrib import admin
from .models import CodingProblem, SampleTestCase, HiddenTestCase, CodingSubmission

class SampleTestCaseInline(admin.TabularInline):
    model = SampleTestCase
    
class HiddenTestCaseInline(admin.TabularInline):
    model = HiddenTestCase

class CodingProblemAdmin(admin.ModelAdmin):
    inlines = [SampleTestCaseInline, HiddenTestCaseInline]

admin.site.register(CodingProblem, CodingProblemAdmin)
admin.site.register(SampleTestCase)
admin.site.register(HiddenTestCase)
admin.site.register(CodingSubmission)
