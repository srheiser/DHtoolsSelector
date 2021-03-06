# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from .models import MappingTools
from .models import UserStories
from django.template import loader
from .models import Inquiry
# Create your views here.
def index(request):
	return HttpResponse("This is the view for dhtools.")
def inquiry(request):
	template = loader.get_template('tools/inquiry.html')
	context = {
		'inquiry_all' : Inquiry.objects.all(),
	}
	return HttpResponse(template.render(context, request))

def inquiry_userstory(request, id):
	select_inquiry = Inquiry.objects.get(pk = id)
	template = loader.get_template('tools/inquiry_userstory.html')
	select_userstories = UserStories.objects.filter(inquiry_id = id)
	context = {
		'select_userstories' : select_userstories,
	}
	return HttpResponse(template.render(context, request))
def detail(request, id):
	select_tool = MappingTools.objects.get(pk = id)
	template = loader.get_template('tools/detail.html')
	context = {
		'select_tool' : select_tool,
	}
#	return HttpResponse("You are looking at the %s." % select_tool.software_name)
	return HttpResponse(template.render(context, request))
def userstory(request, id):
	select_user_story = UserStories.objects.get(pk = id)
	template = loader.get_template('tools/userstory.html')
	context = {
		'select_user_story' : select_user_story,
		'nodes' : UserStories.objects.all(),
	}
	return HttpResponse(template.render(context, request))
def result(request):
#	return HttpResponse("This is the view for the results.")
	story_id = request.GET.get('story')
	select_story = UserStories.objects.get(pk = story_id)
	rec_result = MappingTools.objects.filter(userstories = story_id)
	template = loader.get_template('tools/result.html')
	context = {
		'story_id' : story_id,
		'rec_result' : rec_result,
	}
	return HttpResponse(template.render(context, request))
