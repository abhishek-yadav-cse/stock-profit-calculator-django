from django import forms


class MyForm(forms.Form):
   TickerSymbol = forms.CharField(max_length = 100)
   Allotment = forms.FloatField()
   FinalSharePrice = forms.FloatField()
   SellCommission = forms.FloatField()
   InitialSharePrice = forms.FloatField()
   BuyCommission = forms.FloatField()
   CapitalGainTaxRate = forms.FloatField()
