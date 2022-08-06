from django.shortcuts import render
# Create your views here.z


def dhaj(request):
    return render(request, 'dhaj.html')




def add(request):

    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 +val2

    return render(request, "result.html", {'result': result})