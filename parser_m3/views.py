from django.shortcuts import render

from django.views import generic
from django.http import HttpResponse
from . import models, mashina_parser, forms


class GetParsingM3(generic.FormView):
    template_name = 'parsers_m3/mashina_get_parsing.html'
    form_class = forms.MashinaParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.mashina_parser_data()
            return HttpResponse('<h1>Parsing...</h1>')
        else:
            return super(GetParsingM3, self).post(request, *args, **kwargs)


class MashinaListView(generic.ListView):
    template_name = 'parsers_m3/mashina_list.html'
    model = models.MashinaParser
    context_object_name = 'mashina'

    def get_queryset(self):
        return self.model.objects.all()