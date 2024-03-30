from django.views import generic
from django.http import HttpResponse
from . import models, rezka_parser, forms


class GetParsing(generic.FormView):
    template_name = 'parsers/get_parsing.html'
    form_class = forms.ParserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return HttpResponse('<h1>Parsing...</h1>')
        else:
            return super(GetParsing, self).post(request, *args, **kwargs)


class RezkaListView(generic.ListView):
    template_name = 'parsers/rezka_list.html'
    model = models.Parser
    context_object_name = 'rezka'

    def get_queryset(self):
        return self.model.objects.all()