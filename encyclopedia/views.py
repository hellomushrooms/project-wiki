from django.shortcuts import render
from markdown2 import Markdown
import random

from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html = convert_md_to_html(title)
    if html == None:
        return render(request, "encyclopedia/error.html", {
            "message": "This entry could not be found."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "html": html,
            "title": title
        })
    
def search(request):
    if request.method == "POST":
        search_query = request.POST['q']
        html = convert_md_to_html(search_query)
        substrings = []
        entries = util.list_entries()
        if html == None:
            for entry in entries:
                if search_query.lower() in entry.lower():
                    substrings.append(entry)
            return render(request, "encyclopedia/search_results.html", {
                "substrings": substrings
            })
        else:
            return render(request, "encyclopedia/entry.html", {
                "title": search_query,
                "html": html
            })
        
def addpage(request):
    if request.method == "GET":
        return render(request, "encyclopedia/create_entry.html")
    elif request.method == "POST":
        title = request.POST['p']
        content = request.POST['markdown-content']
        titleexist = util.get_entry(title)        
        if titleexist is None:
            util.save_entry(title, content)
            html = convert_md_to_html(title)
            return render(request, "encyclopedia/entry.html", {
                "title": title,
                "html": html
            })
        else:
            return render(request, "encyclopedia/error.html", {
                "message": "This entry already exists",
            })
        
def editpage(request):
    if request.method == "POST":
        title = request.POST['title']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit_entry.html", {
            "title": title,
            "content": content
        })
    
def saveedit(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['markdown-content']
        util.save_entry(title, content)
        html = convert_md_to_html(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "html": html
        })
    
def randomentry(request):
    entries = util.list_entries()
    title = random.choice(entries)
    content = util.get_entry(title)
    html = convert_md_to_html(title)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "html": html
    })