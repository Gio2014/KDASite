from django.shortcuts import render, render_to_response, RequestContext
from django.template.response import TemplateResponse
from django.template import RequestContext, Template

# New Settings:

from django.views.generic.base import TemplateView

from django.http import HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

# Added EmailForm below
from website.forms import EmailForm
from website.models import EmailTemplate

# Create your views here.

def website(request):
	return TemplateResponse(request, 'kdagroup2.html',)
	
def consulting(request):
	return TemplateResponse(request, 'consulting.html',)
	
def thankyou(request):
	return TemplateResponse(request, 'thankyou.html',)

def thanks(request):
	return TemplateResponse(request, 'thankyou.html',)
	
def sendemail(request):
	if request.method == 'POST':	
		
		form = EmailForm(request.POST)
	
		if form.is_valid():
					
			try:
				subject = request.POST.get('subject')
				message = request.POST.get('message')
				from_email = request.POST.get('sender')
		
				recipients = ['giogomez2010@gmail.com']
		
				send_mail(subject, message, from_email, recipients, fail_silently=False)
	
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
		
	return HttpResponseRedirect('/thanks/')	
	



