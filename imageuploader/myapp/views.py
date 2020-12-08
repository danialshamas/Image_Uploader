from django.shortcuts import render
from . models import Image
from . form import ImageForm
# Create your views here.
def home(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
#  getting all the images
    img = Image.objects.all()
    form = ImageForm()
    return render(request , 'myapp/index.html', {'img': img , 'form': form})