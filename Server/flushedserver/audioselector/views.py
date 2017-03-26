from django.shortcuts import render, redirect

# Create your views here.
from audioselector.forms import MediaForm


def model_form_upload(request):
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(model_form_upload)
    else:
        form = MediaForm()
    return render(request, 'simple_upload.html', {
        'form': form
    })