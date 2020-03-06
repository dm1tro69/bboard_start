from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import BbForm
from .models import Bb, Rubric

# Create your views here.

def index(request):
    bbs = Bb.objects.order_by('-published')
    rubric = Rubric.objects.all()
    return render(request, 'bboard/index.html', {'bbs': bbs, 'rubric': rubric})


def by_rubric(request, rubric_id):
    rubric = Rubric.objects.all()
    bbs = Bb.objects.filter(rubric=rubric_id)
    current_rubric = Rubric.objects.get(pk=rubric_id)
    return render(request, 'bboard/by_rubric.html', {'bbs': bbs, 'rubric': rubric, 'current_rubric': current_rubric})



class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubric'] = Rubric.objects.all()
        return context

