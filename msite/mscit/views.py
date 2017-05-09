from django.conf import settings
from django.shortcuts import render
from django.contrib.sites.shortcuts import get_current_site

#def my_view(request):
   # if settings.SITE_ID == 1:
    
#	return render(request, 'index.html')
	
#def my_view1(request):
 #   if settings.SITE_ID == 3:
    
#	return render(request, 'base.html')	
	

def my_view(request):
    current_site = get_current_site(request)
    if current_site.domain == 'qwerty.com':
	
       return render(request, 'index.html')
	   
    if current_site.domain == 'test1.com':
	
	return render(request, 'base.html') 
	
    if current_site.domain == 'asdfhgh.com':
	
       return render(request, 'view_category.html')
	   
    if current_site.domain == 'ggnj.com':
	
		return render(request, 'view_post.html') 	