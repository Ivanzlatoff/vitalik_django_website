from re import template
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class My_WorkView(TemplateView):
    template_name = 'pages/my_work.html'