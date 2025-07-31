
from django.shortcuts import render
from django.http import HttpResponse
from yaml import serialize
from .models import form
from .form import FormModelForm, FormSerializer
from rest_framework import viewsets
from rest_framework.decorators import action,api_view
from rest_framework.response import Response


def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        class_name = request.POST.get('s_class')
        new_form = form(name=name, age=age, s_class=class_name)
        new_form.save()
        return HttpResponse("Form submitted successfully!")
    

    forms = form.objects.all()
    return render(request, 'index.html', {'forms': forms})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        form.objects.get(id=id).delete()
        return HttpResponse("Form deleted successfully!")
    
    return render(request, 'index.html', {'forms': form.objects.all()})


@api_view(['GET', 'POST','PUT'])
def form_api(request,pk=None):
    if request.method == 'GET':
        forms = form.objects.filter(name__startswith='A').values('name','age')  # Example filter
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)
    

    
    elif request.method == 'POST':
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'Message': 'Form submitted successfully!',
                 'data': serializer.data},
                status=201)
        
    """elif request.method == 'PUT':
        form = form.objects.get(id=pk)
        serializer = FormSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {'Message': 'Form updated successfully!',
                 'data': serializer.data},
                status=200)
        """
    return Response(serializer.errors, status=400)


from django.shortcuts import get_object_or_404

@api_view(['DELETE'])
def delete_form(request, pk):
    form1 = get_object_or_404(form, pk=pk)
    serializer = FormSerializer(form1)
    form1.delete()
    return Response(
        {'Message': 'Form deleted successfully!', 'data': serializer.data},
        status=200
    )

@api_view(['PUT'])
def update_form(request,pk):
    form1 = get_object_or_404(form, pk=pk)
    serializer = FormSerializer(form1, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'Message': 'Form updated successfully!', 'data': serializer.data},
            status=200
        )
    return Response(serializer.errors, status=400)

    
    



