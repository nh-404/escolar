from django.shortcuts import render

def exam(request):

    return render(request, 'exam/exam.html')



def result(request):

    return render(request, 'exam/result.html')


def grade(request):

    return render(request, 'exam/grade.html')


def fees(request):

    return render(request, 'exam/fees.html')