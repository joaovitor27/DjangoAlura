from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import QuerySet
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from apps.gallery.models import Photography


@login_required(login_url='login')
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')
    photography: QuerySet = Photography.objects.order_by('created_at').filter(published=True)
    return render(request, "gallery/index.html", {'photography': photography})


@login_required(login_url='login')
def image(request, id_: int):
    photo: QuerySet | Http404 = get_object_or_404(Photography, id=id_)
    return render(request, "gallery/image.html", {'photo': photo})


@login_required(login_url='login')
def search(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')

    search_ = request.GET.get('search')
    if search is None or not search:
        photography: QuerySet = Photography.objects.order_by('created_at').filter(published=True)
    else:
        photography: QuerySet = Photography.objects.order_by('created_at').filter(
            published=True, name__icontains=search_
        )
    return render(request, "gallery/search.html", {'photography': photography})
