from django.shortcuts import render


def classes(request):

    return render(request, 'classes/class.html')


def total_class(request):

    return render(request, 'classes/total_classes.html')

def attendance(request):

    return render(request, 'classes/attendance.html')



# def (request):

#     return render(request, '.html')

# def (request):

#     return render(request, '.html')