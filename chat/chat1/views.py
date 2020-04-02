from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def head1(request,username):
	use = {username}
	context = {'use' : username}
	#username.save()
	#return HttpResponse("<h1>Welcome {}.</h1>".format(username))
	return render(request,"base1.html",context)


def head(request):
	#use = {username}
	#context = {'use' : username}
	#username.save()
	#return HttpResponse("<h1>Welcome {}.</h1>".format(username))
	return render(request,"base.html")