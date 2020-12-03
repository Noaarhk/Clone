from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Photo


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
