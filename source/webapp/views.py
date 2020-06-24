from django.shortcuts import render
from django.http import HttpResponse



def form_view(request, *args, **kwargs):
    return render(request, 'form.html')


def post_view(request, *args, **kwargs):
    print(request.POST)

    numder = request.POST.get('numder')
    numder2 = request.POST.get('numder2')

    result = request.POST.get('result')


    if result == 'ADD':
        sign = '+'
        results = int(numder) + int(numder2)
    elif result == 'SUB':
        sign = '-'
        results = int(numder) - int(numder2)
    elif result == 'MUL':
        sign = '*'
        results = int(numder) * int(numder2)
    elif result == 'TRUEDIV':
        sign = '/'
        results = int(numder) / int(numder2)



    return render(request, 'post.html',context={
        'numder': numder,
        'sign': sign,
        'numder2': numder2,
        'results': results
    })


