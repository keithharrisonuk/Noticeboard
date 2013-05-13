from django.shortcuts import get_list_or_404, render_to_response
from NoticeboardApp.models import Category, JobType, Notice


def index(request):
    allCategories = get_list_or_404(Category)
    return render_to_response('NoticeboardApp/index.html', {'allCategories': allCategories, 'homeActive': 'active'})


def category(request, categoryId):
    category = Category(id=categoryId)
    allJobs = get_list_or_404(JobType, Category=category)
    return render_to_response('NoticeboardApp/category.html', {'allJobs': allJobs, 'homeActive': 'active'})


def notices(request, jobTypeId):
    jobType = JobType(id=jobTypeId)
    allNotices = get_list_or_404(Notice, JobType=jobType)
    return render_to_response('NoticeboardApp/notices.html', {'allNotices': allNotices, 'homeActive': 'active'})


def AddYourAd(request):
    return render_to_response('NoticeboardApp/AddYourAd.html', {'addYourAddActive': 'active'})