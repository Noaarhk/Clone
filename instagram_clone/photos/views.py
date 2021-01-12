from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from .models import Photo
from .forms import PhotoForm


def ping(request):
    return HttpResponse('Hello!')


def detail(request, pk):
    # photo = Photo.objects.get(pk=pk)
    photo = get_object_or_404(Photo, pk=pk)

    messages = (
        '<p>{pk}번 사진 보여줄게요  </p>'.format(pk=photo.pk),
        '<p>주소는{url}</p>'.format(url=photo.image.url),
        '<p><img src="{url}" /></p>'.format(url=photo.image.url),

    )

    return HttpResponse('\n'.join(messages))


@csrf_exempt
def create(request):
    if request.method == "GET":
        form = PhotoForm()
    elif request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.user.save()
            return redirect(obj)

    ctx = {
        'form': form,
    }

    return render(request, 'photos/edit.html', ctx)
