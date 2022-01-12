from django import forms

class Card(forms.Form):
    card_no = forms.IntegerField(label="card no")
    name = forms.CharField(label="card owner's name", max_length = 200)
    cvc = forms.IntegerField(label="cvc no")