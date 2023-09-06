from django.shortcuts import render, HttpResponse
from markdown2 import Markdown
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)


def entry(request, title):
    html_content = md_to_html(title)
    if html_content == None:
        return render(request, "encyclopedia/error.html")
    else:
        return render(request, "encyclopedia/entry.html")


def create_new_page(request):
    # return HttpResponse("This is Create New Page")
    return render(request, "encyclopedia/create_edit.html")


def random_page(request):
    return HttpResponse("This is Random Page")


def query(request):
    return HttpResponse("This is query page")


def edit_page(request):
    return HttpResponse("This is Edit page")

# def index(request):
#     return HttpResponse("This is homepage")
