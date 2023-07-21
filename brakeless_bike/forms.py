from django import forms


class SpecialPriceForm(forms.Form):
    special_price = forms.DecimalField(label='Special Price', max_digits=8, decimal_places=2)
