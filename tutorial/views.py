from django.shortcuts import render, get_object_or_404
from .models import Tutorial
import markdown
def index(request):
    tutorial_list = Tutorial.objects.all()
    return render(request, 'tutorial/index.html', context={'tutorial_list': tutorial_list})
def detail(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    tutorial.text = markdown.markdown(tutorial.text,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'tutorial/detail.html', context={'tutorial': tutorial})
