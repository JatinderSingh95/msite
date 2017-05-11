from django.conf import settings
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site


def my_view(request):
    current_site = get_current_site(request)
    if current_site.domain == 'qwerty.com':
	
      return render(request, 'index.html')
	   
	
    if current_site.domain == 'test1.com':
	
	return render(request, 'base.html') 
	
    if current_site.domain == 'asdfhgh.com':
	
       return render(request, 'narani.html')
	   
    if current_site.domain == 'ggnj.com':
	
		return render(request, 'nara.html') 	