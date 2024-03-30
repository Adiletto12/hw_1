from django import forms
from . import models, mashina_parser

class MashinaParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('mashina.kg', 'mashina.kg'),
        ('mangalib.me', 'mangalib.me')
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_type']


    def mashina_parser_data(self):
        if self.data['media_type'] == 'mashina.kg':
            car_parser = mashina_parser.get_cars()
            for i in car_parser:
                models.MashinaParser.objects.create(**i)