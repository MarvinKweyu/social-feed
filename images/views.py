from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from images.forms import ImageCreationForm


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
