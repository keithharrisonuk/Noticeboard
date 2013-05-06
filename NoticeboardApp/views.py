from django.shortcuts import get_list_or_404, render_to_response
from NoticeboardApp.models import Category, JobType


def index(request):
    allCategories = get_list_or_404(Category)
    return render_to_response('NoticeboardApp/index.html', {'allCategories': allCategories})


def category(request, categoryId):
    category = Category(id=categoryId)
    allJobs = get_list_or_404(JobType, Category=category)
    return render_to_response('NoticeboardApp/category.html', {'allJobs': allJobs})