from django import forms
from . import models, rezka_parser

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ("rezka.ag", "rezka.ag"),
        ("manas.kg", "manas.kg")
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)


    class Meta:
        fields = ["media_type"]

    def parser_data(self):
        if self.data["media_type"] == "rezka.ag":
            film_parser = rezka_parser.parsing()
            for i in film_parser:
                models.Parser.objects.create(**i)
