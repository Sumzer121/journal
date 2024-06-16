from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import JournalEntry
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import JournalEntryForm
import torch
import logging
import ollama

logging.basicConfig(level=logging.DEBUG)


@login_required
def journal_list(request):
    user = request.user._wrapped if hasattr(request.user, '_wrapped') else request.user
    entries = JournalEntry.objects.filter(user=user)
    form = JournalEntryForm(request.POST or None)

    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid(): 
            new_entry = form.save(commit=False)
            new_entry.user = user
            new_entry.save()
            feedback = generate_feedback(new_entry.content)
            return render(request, 'entries/entry_detail.html', {'entry': new_entry, 'feedback': feedback})
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = JournalEntryForm()

    context = {
        'entries': entries,
        'form': form, 
    }

    return render(request, 'entries/list.html', context)

@login_required
def create_entry(request):
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        entry = JournalEntry.objects.create(user=request.user, title=title, content=content)
        return JsonResponse({'success': True}, status=200)
    else:
        return JsonResponse({'success': False}, status=400)

def custom_login_view(request):
    response = auth_views.login(request, template_name="login.html")
    if request.user.is_authenticated:
        print("User is authenticated:", request.user.username)
        return redirect('entries_list')
    return response

@login_required
def journal_entry_detail(request, entry_id):
    entry = get_object_or_404(JournalEntry, pk=entry_id)
    feedback = generate_feedback(entry.content)
    return render(request, 'entries/entry_detail.html', {'entry': entry, 'feedback': feedback})

def generate_feedback(input_text):
    starting = "Hi I just wrote some journal, and I want you to give some feedback on my journal based on the emotions that the text has"
    ans = "Sure, I'm happy to give you constructive and helpful feedback! Please provide your journal for me!"
    prompt = input_text
    
    feedback = ollama.chat(
        model="llama3",
        messages=[
            {"role": "user", "content": starting},
            {"role": "assistant", "content": ans},
            {"role": "user", "content": prompt}
        ]
    )
    cleaned_feedback = feedback['message']['content']
    return cleaned_feedback
