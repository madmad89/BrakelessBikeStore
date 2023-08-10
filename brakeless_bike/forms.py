from django import forms


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(label='Shipping Address', widget=forms.Textarea(attrs={'rows': 3}))
    billing_address = forms.CharField(label='Billing Address', widget=forms.Textarea(attrs={'rows': 3}))
    card_number = forms.CharField(label='Card Number', max_length=16)
    card_expiry = forms.CharField(label='Card Expiry', max_length=5, help_text='MM/YY')
    card_cvc = forms.CharField(label='Card CVC', max_length=3)
