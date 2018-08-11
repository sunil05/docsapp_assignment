from django.shortcuts import render_to_response

# Create your views here.
def get_app():
    return render_to_response('driver.html', context={})
