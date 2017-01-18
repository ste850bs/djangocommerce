from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string


def switch_menu(request):
	status = "tutti"
	session_status = "null"
	if 'status' in request.session:
		session_status = request.session['status']

	context = {'status':status,
				'session_status':session_status}
	return context


