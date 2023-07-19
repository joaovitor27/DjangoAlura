from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render, get_object_or_404, redirect

from apps.gallery.forms import PhotographyForms
from apps.gallery.models import Photography


@login_required(login_url='login')
def index(request: WSGIRequest) -> HttpResponse | HttpResponsePermanentRedirect | HttpResponseRedirect:
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')
    photography: QuerySet = Photography.objects.order_by('created_at').filter(published=True)
    return render(request, "gallery/index.html", {'photography': photography})


@login_required(login_url='login')
def image(request: WSGIRequest, id_: int) -> HttpResponse | HttpResponsePermanentRedirect | HttpResponseRedirect:
    photo: QuerySet | Http404 = get_object_or_404(Photography, id=id_)
    return render(request, "gallery/image.html", {'photo': photo})


@login_required(login_url='login')
def search(request: WSGIRequest) -> HttpResponse | HttpResponsePermanentRedirect | HttpResponseRedirect:
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')

    search_: str = request.GET.get('search')
    if search is None or not search:
        photography: QuerySet = Photography.objects.order_by('created_at').filter(published=True)
    else:
        photography: QuerySet = Photography.objects.order_by('created_at').filter(
            published=True, name__icontains=search_
        )
    context: dict = {
        'photography': photography
    }
    return render(request, "gallery/index.html", context)


@login_required(login_url='login')
def add_image(request: WSGIRequest) -> HttpResponse | HttpResponsePermanentRedirect | HttpResponseRedirect:
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')

    form_add_images: PhotographyForms = PhotographyForms()

    if request.method == "POST":
        form_add_images: PhotographyForms = PhotographyForms(request.POST, request.FILES)
        if form_add_images.is_valid():
            image_ = form_add_images.save(commit=False)
            image_.user = request.user
            image_.save()
            messages.success(request, 'Imagem adicionada com sucesso!')
            return redirect('image', id_=image_.id)

    context: dict = {
        'form_add_images': form_add_images
    }

    return render(request, "gallery/add-image.html", context)


@login_required(login_url='login')
def edit_image(request: WSGIRequest, id_: int) -> HttpResponse | HttpResponsePermanentRedirect | HttpResponseRedirect:
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')

    photo: QuerySet | Http404 = get_object_or_404(Photography, id=id_)
    form_edit_images: PhotographyForms = PhotographyForms(instance=photo)
    if request.method == "POST":
        form_edit_images: PhotographyForms = PhotographyForms(request.POST, request.FILES, instance=photo)
        if form_edit_images.is_valid():
            form_edit_images.save()
            messages.success(request, 'Imagem editada com sucesso!')
            return redirect('image', id_=id_)

    context: dict = {
        'image_id': id_,
        'form_edit_images': form_edit_images
    }
    return render(request, "gallery/edit-image.html", context)


@login_required(login_url='login')
def delete_image(request: WSGIRequest, id_: int) -> HttpResponsePermanentRedirect | HttpResponseRedirect:
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')

    photo: QuerySet | Http404 = get_object_or_404(Photography, id=id_)
    photo.published = False
    photo.save()
    messages.success(request, 'Imagem deletada com sucesso!')
    return redirect('index')


@login_required(login_url='login')
def filter_category(request: WSGIRequest,
                    category: str) -> HttpResponse | HttpResponsePermanentRedirect | HttpResponseRedirect:

    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')

    photography: QuerySet = Photography.objects.order_by('created_at').filter(published=True, category=category)
    context: dict = {
        'photography': photography,
    }
    return render(request, "gallery/index.html", context)
