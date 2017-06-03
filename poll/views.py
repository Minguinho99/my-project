from django.shortcuts import render

def post_list(request):
    return render(request, 'poll/post_list.html', {})
