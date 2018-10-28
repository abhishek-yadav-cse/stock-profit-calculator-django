from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie


# from .forms import MyForm
from .forms import HomeForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.method == 'POST':   
            form = HomeForm(request.POST) 
            if form.is_valid():
                    TickerSymbol = form.cleaned_data['TickerSymbol']
                    Allotment = form.cleaned_data['Allotment']
                    FinalSharePrice = form.cleaned_data['FinalSharePrice']
                    SellCommission = form.cleaned_data['SellCommission']
                    InitialSharePrice = form.cleaned_data['InitialSharePrice']
                    BuyCommission = form.cleaned_data['BuyCommission']
                    CapitalGainTaxRate = form.cleaned_data['CapitalGainTaxRate']


                    #########################   REPORT GENERATION ############################
                    Proceeds= Allotment*FinalSharePrice
                    print ("Proceeds")
                    print ("$"+ str( Proceeds))

                    #capitalGain1 = ( ( Selling Price × Number of Shares ) - Selling Commission ) - ( ( Buying Price × Number of Shares ) + Buying Commission)
                    capitalGain1 = ((FinalSharePrice * Allotment) - SellCommission) - ((InitialSharePrice * Allotment) + BuyCommission)
                    #print (capitalGain1)
                    print(" ")

                    #Cost (Allotment x Initial Share Price + commissions + Tax on Capital Gain)
                    Cost= (Allotment*InitialSharePrice+(SellCommission+BuyCommission)+(CapitalGainTaxRate/100 )*capitalGain1)
                    print ("Cost")
                    print ("$"+ str( Cost))
                    print("")

                    print ("Cost details: ")
                    print("Total Purchase Price")
                    TotalPurchasePrice = Allotment * InitialSharePrice
                    print(Allotment * InitialSharePrice)
                    print("Buy Commission=", BuyCommission)
                    print("Sell Commission=", SellCommission)
                    print ("Tax on Capital Gain = " , ((CapitalGainTaxRate/100) *capitalGain1))
                    TaxonCapitalGain = (CapitalGainTaxRate/100) *capitalGain1

                    print("")

                    #Net Profit (in dollars)
                    NetProfit = Proceeds - Cost
                    print ("Net Profit")
                    print ("$"+ str( NetProfit))
                    print(" ")

                    #Return on investment (in %), Net Profit / Total Investment * 100.
                    ReturnonInvestment = (NetProfit / Cost *100) 
                    print("Return on Investment:")
                    print (str(ReturnonInvestment )+ "%")
                    print(" ")

                    #Break even price (in dollars) 2500+10+15/100
                    ToBreakEven= ((Allotment *InitialSharePrice) + BuyCommission +  SellCommission )/100
                    print("To break even, you should have a final share price of")
                    print ( "$"+ str(ToBreakEven))
                    print(" ")
                    

                    args = {"form": form, "Proceeds" : Proceeds, "Cost": Cost, "TotalPurchasePrice": TotalPurchasePrice, "BuyCommission": BuyCommission, "SellCommission": SellCommission, "TaxonCapitalGain": TaxonCapitalGain, "NetProfit": NetProfit, "ReturnonInvestment": ReturnonInvestment, "ToBreakEven": ToBreakEven, "Allotment": Allotment, "InitialSharePrice": InitialSharePrice}
            
        return render(request, "result.html", args)