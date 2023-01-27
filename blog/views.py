from django.shortcuts import render


def blog_list_view(request):
    context = {}
    return render(request, 'index.html', context)
