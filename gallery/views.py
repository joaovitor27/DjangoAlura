from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import render, get_object_or_404

from gallery.models import Photography


def index(request):
    photography: QuerySet = Photography.objects.order_by('created_at').filter(published=True)
    return render(request, "gallery/index.html", {'photography': photography})


def image(request, id_: int):
    photo: QuerySet | Http404 = get_object_or_404(Photography, id=id_)
    return render(request, "gallery/image.html", {'photo': photo})


def search(request):
    search_ = request.GET.get('search')
    if search is None or not search:
        photography: QuerySet = Photography.objects.order_by('created_at').filter(published=True)
    else:
        photography: QuerySet = Photography.objects.order_by('created_at').filter(
            published=True, name__icontains=search_
        )
    return render(request, "gallery/search.html", {'photography': photography})
