from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Darryl Abysha Artapradana Subiyanto',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)

# Create your views here.
