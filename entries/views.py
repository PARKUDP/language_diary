# entries/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Entry
from .forms import EntryForm
from django.contrib.auth.decorators import login_required

@login_required
def entry_list(request):
    entries = Entry.objects.filter(user=request.user).order_by('-date_posted')
    return render(request, 'entries/entry_list.html', {'entries': entries})

@login_required
def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk, user=request.user)  # 現在のユーザーの日記のみを取得
    return render(request, 'entries/entry_detail.html', {'entry': entry})

@login_required
def entry_create(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user  # 現在のログインユーザーを設定
            entry.save()
            return redirect('entry_list')
    else:
        form = EntryForm()
    return render(request, 'entries/entry_form.html', {'form': form})

@login_required
def entry_update(request, pk):
    entry = get_object_or_404(Entry, pk=pk, user=request.user)  # 現在のユーザーの日記のみを取得
    if request.method == "POST":
        form = EntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry_detail', pk=pk)
    else:
        form = EntryForm(instance=entry)
    return render(request, 'entries/entry_form.html', {'form': form})

@login_required
def entry_delete(request, pk):
    entry = get_object_or_404(Entry, pk=pk, user=request.user)  # 現在のユーザーの日記のみを取得
    if request.method == "POST":
        entry.delete()
        return redirect('entry_list')
    return render(request, 'entries/entry_confirm_delete.html', {'entry': entry})
