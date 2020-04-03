from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from PIL import Image
import time
import os

# Create your views here.

set_quality = 0


def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        quality = request.POST['quality_slider']
        set_quality = quality
        if form.is_valid():
            # Save Original Image and get ID
            add = form.save()
            i_id = add.id
            # quality = form.cleaned_data['quality']
            type = form.cleaned_data['image_format']

            # From Id get original Image path for further conversion
            og_image = Images.objects.get(id=add.id)
            image_url = og_image.original_img

            # Opening image and applying convesion operation

            img = Image.open(image_url)
            if(type == None):
                type = img.format

            if img.mode != 'RGB':
                img = img.convert('RGB')
            new_name = int(time.time())
            print(quality, "dsds")

            img.save('media/converted/{}.{}'.format(new_name, type),
                     quality=int(set_quality))

            # Calculating inage sizes
            original_size = os.stat('media/'+str(image_url)).st_size
            converted_size = os.stat(
                'media/converted/{}.{}'.format(new_name, type)).st_size

            # Updating all data
            Images.objects.filter(id=i_id).update(converted_img='converted/{}.{}'.format(
                new_name, type), converted_size=converted_size, original_size=original_size)

            return HttpResponseRedirect(request.path_info)
    # To show Image List
    form = ImageForm()
    images = Images.objects.all().order_by('id').reverse()
    context = {
        'form': form,
        'images': images
    }
    return render(request, 'index.html', context)
   