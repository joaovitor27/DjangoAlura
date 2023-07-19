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
    """
    The index function is responsible for rendering the index page of the gallery app.
    It will return a HttpResponse object with an HTML template rendered, or it will redirect to another page.

    :param request: WSGIRequest: Get the request object
    :return: A httpresponse | httpresponsepermanentredirect | httpresponseredirect
    :doc-author: Trelent
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')
    photography: QuerySet = Photography.objects.order_by('created_at').filter(published=True)
    return render(request, "gallery/index.html", {'photography': photography})


@login_required(login_url='login')
def image(request: WSGIRequest, id_: int) -> HttpResponse | HttpResponsePermanentRedirect | HttpResponseRedirect:
    """
    The image function is a view that takes in an HTTP request and the id of a photo,
    and returns either an HttpResponse object with the image.html template rendered to it, or
    an HttpResponsePermanentRedirect or HttpResponseRedirect object if there was no such photo.

    :param request: WSGIRequest: Get the request object
    :param id_: int: Get the id of the image that was clicked on
    :return: A httpresponse, httpresponsepermanentredirect or a httpresponseredirect
    :doc-author: Trelent
    """
    photo: QuerySet | Http404 = get_object_or_404(Photography, id=id_)
    return render(request, "gallery/image.html", {'photo': photo})


@login_required(login_url='login')
def search(request: WSGIRequest) -> HttpResponse | HttpResponsePermanentRedirect | HttpResponseRedirect:
    """
    The search function is responsible for searching the database for a specific photography.
    It receives a request from the user and returns an HttpResponse with all of the photography that match
    the search criteria.

    :param request: WSGIRequest: Get the request data from the user
    :return: The same as the index function
    :doc-author: Trelent
    """

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
    """
    The add_image function is responsible for adding a new image to the database.
    It receives an HTTP request from the user, and if it's a POST request, it will
    validate the form data and save it to the database. If not, then we just render
    the add-image template with an empty form.

    :param request: WSGIRequest: Get the request object
    :return: A httpresponseredirect object, which is a subclass of httpresponse
    :doc-author: Trelent
    """

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
    """
    The edit_image function is responsible for editing an image.
    It receives a request and the id of the image to be edited, then it checks if the user is authenticated. If not,
    it redirects him to login page with an error message. Otherwise, it gets the photo object from database or returns
    404 if there's no such object in database and creates a form instance with this photo as its instance parameter so
    that we can edit this specific photo instead of creating another one (which would be useless).
    Then we check if request method is POST:

    :param request: WSGIRequest: Get the request object from the user
    :param id_: int: Get the image id from the url
    :return: A httpresponseredirect
    :doc-author: Trelent
    """

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
    """
    The delete_image function is responsible for deleting a photo from the database.
    It takes in a request and an id_ as parameters, and returns either an HttpResponsePermanentRedirect or
    an HttpResponseRedirect. If the user is not authenticated, it will return an error message to them
    and redirect them to the login page. Otherwise, it will get the photo with that id_ from our database
    and set its published field to False (which means that it won't be displayed on our website anymore).
    It then saves this change in our database and returns a success message along with a redirection back to index

    :param request: WSGIRequest: Get the request object, which contains information about the current http request
    :param id_: int: Get the id of the image that will be deleted
    :return: A httpresponsepermanentredirect or a httpresponseredirect
    :doc-author: Trelent
    """
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
    """
    The filter_category function is responsible for filtering the photography objects by category.
    It receives a request and a category as parameters, and returns an HttpResponse object with the
    filtered photography objects.

    :param request: WSGIRequest: Access the request object
    :param category: str: Filter the photos by category
    :return: A httpresponse or a httpresponsepermanentredirect or a httpresponseredirect
    :doc-author: Trelent
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Você precisa estar logado para acessar essa página!')
        return redirect('login')

    photography: QuerySet = Photography.objects.order_by('created_at').filter(published=True, category=category)
    context: dict = {
        'photography': photography,
    }
    return render(request, "gallery/index.html", context)
