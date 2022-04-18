from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'ghblog/index.html'


class HolyChild(TemplateView):
    template_name = 'ghblog/holychild.html'


class Wesley(TemplateView):
    template_name = 'ghblog/wesley.html'

class Motown(TemplateView):
    template_name = 'ghblog/motown.html'

class More(TemplateView):
    template_name = 'ghblog/more.html'