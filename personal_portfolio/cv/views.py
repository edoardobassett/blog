from django.shortcuts import render
from cv.models import Field
from django.db.models import F

def cv(request):
    #fields = Field.objects.all().order_by(F('end_date').desc(nulls_first=True), '-start_date')
    work_experience = Field.objects.filter(category="work-experience").order_by(F('end_date').desc(nulls_first=True), '-start_date')
    education = Field.objects.filter(category="education").order_by(F('end_date').desc(nulls_first=True), '-start_date')
    milestones = Field.objects.filter(category="milestones").order_by(F('end_date').desc(nulls_first=True), '-start_date')
    languages = Field.objects.filter(category="languages").order_by(F('end_date').desc(nulls_first=True), '-start_date')

    return render(request, 'cv.html', {'work_experience' : work_experience, 'education' : education, 'milestones' : milestones, 'languages' : languages})