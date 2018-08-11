from django.shortcuts import render_to_response


def get_dashboard():
    return render_to_response('customerapp.html')