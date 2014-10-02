from django.shortcuts import render, render_to_response, RequestContext

# Create your views here.

def test(request):
	return render_to_response("testPage.html", locals(), context_instance=RequestContext(request))