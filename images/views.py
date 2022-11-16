from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from images.forms import ImageCreationForm
from images.models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreationForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            # assign current user to the image
            new_item.user = request.user
            new_item.save()
            messages.success(request, "Image added successfully")
            # go to the detail page
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreationForm(request.GET)
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/detail.html', {'section': 'images', 'image': image})