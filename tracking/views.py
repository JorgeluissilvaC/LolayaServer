from django.shortcuts import render
from moduls import query as p
#http://181.192.218.153/into?q=ST300UEX;123456;2.0;5.4;04052018015055;C8545;12.122154;-10.15465;64.15;85;4;1;451;13.24;0;1;350;12;4.1;1;12.12

def test(request):
    query = request.GET.get('q', '')
    p.saveData(query)
    return render(request, 'tracking/into.html')