from django.shortcuts import render

# Create your views here.
def list_view(request):
    qs = final.objects.all()
    context = {}
    return render(request, 'final/list.html',context)
def detail_view(request, pk):
