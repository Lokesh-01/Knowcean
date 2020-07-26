from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import util
import markdown2
from django.contrib import messages
import random



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request,title):
    markdown_code = util.get_entry(title)
    if markdown_code is None:
        return render(request,'encyclopedia/error.html',{
            "error":"the page you are looking for is not found"
        })
    else:
        markdown_code=util.get_entry(title)
        converted_code=markdown2.markdown(markdown_code)
        return render(request,'encyclopedia/title.html',{
            "content":converted_code,"title":title
        })
def  search(request):
    if request.method=='POST':
        query =request.POST["q"]
        result=util.get_entry(query)
        if result:
            return HttpResponseRedirect("wiki/"+query)
        else:
            entriess=util.list_entries()
            search_entries = [i for i in entriess if query in i]
            if search_entries:
                return render(request,'encyclopedia/index.html',{
                    "entries":search_entries
                })
            else:
                return render(request,"encyclopedia/error.html",{
                    "error":"The page you are looking for is not found"
                })
def newentry(request):
    if request.method=='POST':
        entry_title= request.POST["entry_title"]
        entry_content=request.POST["entry_content"]
        entries_list=util.list_entries()
        if (entry_title in entries_list):
            messages.error(request,'An Entry with this title already exists')
            return render(request,"encyclopedia/newfile.html")
        else:
            util.save_entry(entry_title,entry_content)
            markdown_code=util.get_entry(entry_title)
            converted_code=markdown2.markdown(markdown_code)
            return render(request,'encyclopedia/title.html',{
                "content":converted_code,"title":entry_title
            })
    else:
        entry_title=""
        entry_content=""
        return render(request,"encyclopedia/newfile.html")

def editpage(request,title):
    if request.method=='POST':
        markdown_content=util.get_entry(title)
        return render(request,"encyclopedia/editarea.html",{
            "content":markdown_content ,"title":title
        })
def editedpage(request,title):
    if request.method=='POST':
        edited_content=request.POST["edit_area"]
        util.save_entry(title,edited_content)
        markdown_code=util.get_entry(title)
        converted_code=markdown2.markdown(markdown_code)
        return render(request,'encyclopedia/title.html',{
            "content":converted_code,"title":title
        })

def random_entry(request):
    entry_list=util.list_entries()
    r_entry=random.choice(entry_list)
    return HttpResponseRedirect("wiki/"+r_entry)
