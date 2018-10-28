from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie


from .forms import MyForm

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class AboutPageView(TemplateView):
    template_name = "about.html"

class ResultPageView(TemplateView):
    template_name = "result.html"
    @ensure_csrf_cookie
    def result(request):
        # if request.method == "POST":
        #     #Get the posted form
        #     MyStockForm = MyForm(request.POST)
        if request.method == 'POST':   
            form = MyForm(request.POST) 
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
                    capitalGain1 = ((FinalSharePrice * Allotment) - SellCommission) - ((InitialSharePrice * Allotment) + BuyComission)
                    #print (capitalGain1)
                    print(" ")

                    #Cost (Allotment x Initial Share Price + commissions + Tax on Capital Gain)
                    Cost= (Allotment*InitialSharePrice+(SellCommission+BuyComission)+(CapitalGainTaxRate/100 )*capitalGain1)
                    print ("Cost")
                    print ("$"+ str( Cost))
                    print("")

                    print ("Cost details: ")
                    print("Total Purchase Price")
                    TotalPurchasePrice = Allotment * InitialSharePrice
                    print(Allotment * InitialSharePrice)
                    print("Buy Commission=", BuyComission)
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
                    ToBreakEven= ((Allotment *InitialSharePrice) + BuyComission +  SellCommission )/100
                    print("To break even, you should have a final share price of")
                    print ( "$"+ str(ToBreakEven))
                    print(" ")
                    return HttpResponseRedirect('/result/')
            
        # return render(request, 'result.html', {"Proceeds" : Proceeds, "Cost": Cost, "TotalPurchasePrice": TotalPurchasePrice, "BuyCommission": BuyCommission, "SellCommission": SellCommission, "TaxonCapitalGain": TaxonCapitalGain, "NetProfit": NetProfit, "ReturnonInvestment": ReturnonInvestment, "ToBreakEven": ToBreakEven})