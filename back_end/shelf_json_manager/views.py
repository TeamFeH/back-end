import json

from django.http import HttpResponse
from shelf_json_manager.models import Shelf, Drawer, Pdf
from django.core.urlresolvers import reverse
from wand.image import Image
import logging


def index(request):
    return HttpResponse("Please add the shlef name to the url to retrive the\
        json")


def get_json(request, shelf_name):
    response_data = {}
    shelf = Shelf.objects.filter(name=shelf_name)[0]
    response_data['name'] = shelf.name
    response_data['drawers'] = []

    for drawer in shelf.drawer_set.all():
        pdfs = []
        for pdf in drawer.pdf_set.all():
            thumb_url = reverse('pdf_thumbnail', kwargs={'pdf_name_arg': pdf.pdf_name})
            pdfs.append({
                'name': pdf.pdf_name,
                'image_url': pdf.pdf_file.url,
                'thumbnail_url': thumb_url})
        response_data['drawers'].append({
            "name": drawer.name,
            "pdfs": pdfs})

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json")


def pdf_thumbnail(request, pdf_name_arg):
    pdf = Pdf.objects.get(pdf_name=pdf_name_arg)
    with Image(filename=pdf.pdf_file.path) as img:
        img.format = 'jpeg'
        img.sample(20, 20)
        response = HttpResponse(content_type="image/jpeg")
        img.save(response)
        return response

