from django import forms

class AddNewItemForm(forms.Form):
    url = forms.CharField(max_length=600)
    requested_price = forms.IntegerField()
    email =form.CharField(max_length =400)
