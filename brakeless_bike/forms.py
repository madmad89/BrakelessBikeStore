from django import forms


class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(label='Shipping Address', widget=forms.Textarea(attrs={'rows': 3}))
    billing_address = forms.CharField(label='Billing Address', widget=forms.Textarea(attrs={'rows': 3}))
    city = forms.CharField(label='City', max_length=50)
    card_number = forms.CharField(label='Card Number', max_length=16)
    card_expiry = forms.CharField(label='Card Expiry', max_length=5, help_text='MM/YY')
    card_cvc = forms.CharField(label='Card CVC', max_length=3)

    # # Additional options
    # subscribe_to_newsletter = forms.BooleanField(label='Subscribe to Newsletter', required=False)
    #
    # # You can add more fields as needed
    #
    # def clean_card_number(self):
    #     card_number = self.cleaned_data['card_number']
    #     if not card_number.isdigit():
    #         raise forms.ValidationError("Card number must only contain digits.")
    #     return card_number
    #
    # def clean_zip_code(self):
    #     zip_code = self.cleaned_data['zip_code']
    #     if not zip_code.isdigit():
    #         raise forms.ValidationError("ZIP code must only contain digits.")
    #     return zip_code
