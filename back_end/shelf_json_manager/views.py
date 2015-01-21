import json

from django.http import HttpResponse
from shelf_json_manager.models import Shelf, Drawer, Pdf


def index(request):
    return HttpResponse("Please add the shlef name to the url to retrive the\
        json")


def get_json(request, shelf_name):
    response_data = {}
    shelf = Shelf.objects.filter(name=shelf_name)[0]
    response_data['name'] = shelf.name
    response_data['drawers'] = []

    for drawer in shelf.drawer_set.all():
        pdf_urls = []
        for pdf_url in drawer.pdf_set.all():
            pdf_urls.append(pdf_url.pdf_file.url)
        response_data['drawers'].append({
            "name": drawer.name,
            "pdf_urls": pdf_urls})

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json")
