from django.shortcuts import render
from .models import Entry

def entry_list(request):
    entries = Entry.objects.all().order_by('-date_posted')
    return render(request, 'entries/entry_list.html', {'entires': entries})

def entry_detail(request, pk):
    entry = Entry.objects.get(pk=pk)
    return render(request, 'entries/entry_detail.html', {'entry': entry})